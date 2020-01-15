from pymongo import MongoClient
from datetime import datetime
from os import environ


class Database:
    client = MongoClient(environ.get("MONGO_HOSTNAME") or "localhost", 27017)
    db = client[environ.get("MONGO_DB") or "test"]
    collection = db[environ.get("MONGO_COLLECTION") or "test"]

    def insert(self, doc):
        return str(self.collection.insert_one(doc).inserted_id)

    def get(self, _id, projection=None):
        return self.collection.find_one(_id, projection=projection)

    def get_all(self, projection=None):
        return [doc for doc in self.collection.find()]


test_doc = {
    "author": "Dmitriy Diachkov",
    "text": "Sample text",
    "timestamp": datetime.utcnow(),
}

if __name__ == "__main__":
    db = Database()
    print(db.insert(test_doc))
