import motor.motor_asyncio
from decouple import config

# name of the database
MONGODB_DB = config('DB_NAME', default='news_api')

# name of the collection
MONGODB_COLLECTION = config('COLLECTION_NAME', default='news')

#  mongodb://<dbUser>:<dbUserPassword>@host:port
MONGO_DETAILS = config('MONGO_DETAILS', default='mongodb://127.0.0.1:27017')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client[MONGODB_DB]

news_collection = database[MONGODB_COLLECTION]


async def retrieve_news(source: str = None):
    news_list = []

    if source:
        async for news in news_collection.find({'source': source}):
            news_list.append(news_helper(news))
    else:
        async for news in news_collection.find():
            news_list.append(news_helper(news))

    return news_list


# helpers
def news_helper(news) -> dict:
    """Parsing the results from a database query into a Python dict."""
    return {
        'id': str(news['_id']),
        'title': news['title'],
        'link': news['link'],
        'image_url': news['image_url'],
        'source': news['source'],
    }
