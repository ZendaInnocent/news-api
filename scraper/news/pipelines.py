# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

from . import settings


class NewsPipeline:
    def process_item(self, item, spider):
        return item


class MongoDBPipeline:

    def __init__(self):
        connection = pymongo.MongoClient(
            settings.MONGO_DETAILS
        )
        db = connection[settings.MONGODB_DB]
        self.collection = db[settings.MONGODB_COLLECTION]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem(f'Missing {data}')
        if valid:
            self.collection.insert(dict(item))
        return item
