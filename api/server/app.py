from datetime import timedelta

from decouple import config
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_pagination import add_pagination

from .auth import authenticate_user, get_password_hash
from .database import database
from .models import Token, User
from .routes import router
from .tokens import create_access_token

# openssl rand -hex 32
SECRET_KEY = config('JWT_SECRET')
ALGORITHM = config('JWT_ALGORITHM', default='HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = 30

description = """
# News API consisting various sources from Tanzania.

## News
You can read news.
"""

app = FastAPI(
    title='Tanzania News API',
    description=description,
    version='0.0.1',
    license_info={
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
    },
    redoc_url=None,
)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(router, tags=['News'], prefix='/news')

@app.get('/', tags=['Root'])
async def root():
    return {'message': 'Welcome to Tanzania News API'}


@app.post('/users/signup', response_model=User, tags=['Users'])
async def create_user(user: User):
    users_collection = database['users']
    user_dict = dict({
        'username': user.username,
        'password': user.password,
        'hashed_password': get_password_hash(user.password),
    })
    await users_collection.insert_one(user_dict)
    return user_dict


@app.post('/users/login', response_model=Token, tags=['Users'])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=400,
            detail='Incorrect username or password'
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user.username}, expires_delta=access_token_expires
    )

    return {'access_token': access_token, 'token_type': 'bearer'}


add_pagination(app)
