from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import router

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
