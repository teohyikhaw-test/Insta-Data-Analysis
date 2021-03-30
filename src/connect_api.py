from pymongo import MongoClient
import http.client

def connectmongo():
    username="XXXXX"
    password="XXXXX"
    client = MongoClient("mongodb+srv://"+username+":"+password+"@fbm1.awjp0.mongodb.net/test1?retryWrites=true&w=majority")
    return client

def connectinstaapi():
    conn = http.client.HTTPSConnection("instagramdimashirokovv1.p.rapidapi.com")
    key="XXXXX"
    headers = {
        'x-rapidapi-key': key,
        'x-rapidapi-host': "InstagramdimashirokovV1.p.rapidapi.com"
    }

    return conn, headers
