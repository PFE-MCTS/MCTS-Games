import pymongo
from pymongo import MongoClient

client = MongoClient()


def connection(database, localhost="localhost", port=27017):
    client = MongoClient(host=localhost, port=port)
    db = client[database]
    return db
    print("connected successfuly to the database:", client)


def addData(database, collection, data):
    pass


def findNode(database, collection, data):
    pass



connection("tictactoe")