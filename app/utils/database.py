from os import environ

from bson.objectid import ObjectId
from pymongo import MongoClient, errors

# TODO: Rewrite DB connector
class Database:
    client = MongoClient(
        f"mongodb+srv://{environ.get('MONGO_USERNAME')}:{environ.get('MONGO_PASSWORD')}"
        f"@{environ.get('MONGO_HOSTNAME') or '127.0.0.1:27017'}/?retryWrites=true&w=majority&authSource=admin")
    db = client[environ.get("MONGO_DB") or "ci_tests"]
    collection = db[environ.get("MONGO_COLLECTION") or "ci"]

    @staticmethod
    def __serialize_id(_id):
        return ObjectId(_id)

    def insert(self, doc):
        return str(self.collection.insert_one(doc).inserted_id)

    def healthcheck(self):
        try:
            self.client.server_info()
            return True
        except errors.PyMongoError as err:
            return err

    def get(self, _id, projection=None):
        _id = self.__serialize_id(_id)
        return self.collection.find_one(_id, projection=projection)

    def get_all(self, projection=None):
        return [doc for doc in self.collection.find(projection=projection)]

    def update(self, _id, data):
        _id = self.__serialize_id(_id)
        return self.collection.update_one({"_id": _id}, {"$set": data}).acknowledged

    def delete(self, _id):
        _id = self.__serialize_id(_id)
        return self.collection.delete_one({"_id": _id}).acknowledged
