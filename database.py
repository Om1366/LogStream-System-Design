from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["logstream"]

logs_collection = db["logs"]


def save_log(log):
    logs_collection.insert_one(log)


def get_logs():
    return list(logs_collection.find())