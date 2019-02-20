import pymongo
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client['tsubasa']
users_collection = db['status']

user = {"userId": "12345", "status": 1, "time": datetime.now()}

user_id = users_collection.insert_one(user).inserted_id
print(user_id)
client.close()
