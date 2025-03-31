from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGODB_URI"))

db = client["todo_app"]
