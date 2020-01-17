from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
from os import environ


class Database:
    client = MongoClient(environ.get("MONGO_HOSTNAME") or "localhost", 27017)
    db = client[environ.get("MONGO_DB") or "testtest"]
    collection = db[environ.get("MONGO_COLLECTION") or "test"]

    @staticmethod
    def __serialize_id(_id):
        return ObjectId(_id)

    def insert(self, doc):
        return str(self.collection.insert_one(doc).inserted_id)

    def get(self, _id, projection=None):
        _id = self.__serialize_id(_id)
        return self.collection.find_one(_id, projection=projection)

    def get_all(self, projection=None):
        return [doc for doc in self.collection.find()]

    def update(self, _id, data):
        _id = self.__serialize_id(_id)
        return self.collection.update_one({"_id": _id}, {"$set": data}).acknowledged

    def delete(self, _id):
        _id = self.__serialize_id(_id)
        return self.collection.delete_one({"_id": _id}).acknowledged


test_doc = {
    "author": "Dmitriy Diachkov",
    "text": "Sample text",
    "timestamp": datetime.utcnow(),
}

if __name__ == "__main__":
    db = Database()
    a = db.insert(test_doc)
    print(db.update(a, {"text": "updated sample text"}))
