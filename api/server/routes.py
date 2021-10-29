from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params, paginate

from .database import retrieve_news
from .models import ResponseModel

router = APIRouter()


@router.get('/', response_description='News retrieved', response_model=Page)
async def get_news():
    news = await retrieve_news()
    if news:
        # return ResponseModel(news, 'News retrieved successfully')
        return paginate(news)
    return ResponseModel(news, 'Empty list returned')


@router.get('/{source}')
async def get_source_news(source, params: Params = Depends()):
    news = await retrieve_news(source)
    if news:
        return paginate(news, params)
    return ResponseModel(news, f'No news returned from source - {source}')
