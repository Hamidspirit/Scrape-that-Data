# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import hashlib
from itemadapter import ItemAdapter
import pymongo
from scrapy.exceptions import DropItem 

# This class will be the Load part of program , helping to insert into database
class BooksPipeline:
    COLLECTION_NAME = "book"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get("MONGO_URI"),
            mongo_db = crawler.settings.get("MONGO_DATABASE"),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # This will make sure duplicate items dont get added to DB
        item_id = self.compute_item_id(item)
        if self.db[self.COLLECTION_NAME].find_one({"_id": item_id}):
            raise DropItem(f"Duplicate item found: {item}")
        else:
            item["_id"] = item_id
            self.db[self.COLLECTION_NAME].insert_one(ItemAdapter(item).asdict())
            return item

        # this piece of code is in case the url that im using as _id stays same but
        # the content changes, this block of code updates other fileds but it does not add 
        # duplicate.
        # it also bypasses item adapter so i dont have to update my BookItem
        # item_id = self.compute_item_id(item)
        # item_dict = ItemAdapter(item).asdict()

        # self.db[self.COLLECTION_NAME].update_one(
        #     filter={"_id": item_id},
        #     update={"$set": item_dict},
        #     upsert=True
        # )

        # return item

    def compute_item_id(self, item):
        url = item["url"]
        return hashlib.sha256(url.encode("utf-8")).hexdigest()