import pymongo
from pymongo import MongoClient


# Status : {1=Share,2=Join,3=End,Unclear=4}

class Users:
    client = None
    db = None
    collection = None

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['tsubasa']
        self.collection = self.db['users']

    def findBy_username(self, username):
        user = self.collection.find_one({"username": username})
        return user

    def findBy_chatId(self, chatId):
        user = self.collection.find_one({"chatId": chatId})
        return user

    def count_share(self):
        count = self.collection.count_documents({"status": 1})
        return count

    def count_join(self):
        count = self.collection.count_documents({"status": 2})
        return count

    def count_unclear(self):
        count = self.collection.count_documents({"status": 4})
        return count

    def find_start_share(self):
        matches = self.collection.find({"status": 1}).sort("username", pymongo.ASCENDING)
        return matches

    def find_start_join(self):
        matches = self.collection.find({"status": 2}).sort("username", pymongo.ASCENDING)
        return matches

    def find_unclear(self):
        matches = self.collection.find({"status": 4}).sort("username", pymongo.ASCENDING)
        return matches

    def update_status(self, chatId, status):
        query = {"chatId": chatId}
        newvalues = {"$set": {"status": status}}
        self.collection.update_one(query, newvalues)

    def close_connection(self):
        self.client.close()

    def find_all(self):
        matches = self.collection.find()
        return matches
