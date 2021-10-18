from fastapi import APIRouter, Depends

from .database import retrieve_all_news
from .models import ResponseModel

router = APIRouter()


@router.get('/', response_description='News retrieved')
async def get_news():
    news = await retrieve_all_news()
    if news:
        return ResponseModel(news, 'News retrieved successfully')
    return ResponseModel(news, 'Empty list returned')
