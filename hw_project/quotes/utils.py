from pymongo import MongoClient


def get_mongodb():
    client = MongoClient('mongodb://localhost')

    db = client.HW10
    return db