import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['tsubasa']
users_collection = db['users']

user = {"username": "MohammadR1271", "chatId": 75594079, "status": 3}

user_id = users_collection.insert_one(user).inserted_id
print(user_id)
client.close()
