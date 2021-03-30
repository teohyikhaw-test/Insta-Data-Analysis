from pymongo import MongoClient

def connectmongo():
    username="FBM1-A1"
    password="6dXaxb30FcoDvEAW"
    client = MongoClient("mongodb+srv://"+username+":"+password+"@fbm1.awjp0.mongodb.net/test1?retryWrites=true&w=majority")
    return client

