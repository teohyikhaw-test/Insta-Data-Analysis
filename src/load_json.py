import json
import pandas
from src.connect_mongo import *

def upload_json(tag,filename):
    client=connectmongo()

    if tag=="hashtag":
        db = client["hashtag"]

    elif tag=="user":
        db = client["user"]

    col = db[tag]

    # Loading or Opening the json file
    with open(filename) as json_file:
        data = json.load(json_file)

    data=data["edges"]

    # Inserting the loaded data in the Collection
    # if JSON contains data more than one entry
    # insert_many is used else insert_one is used
    if isinstance(data, list):
        col.insert_many(data)
    else:
        col.insert_one(data)


def download_database(database,collection,filename):
    client=connectmongo()
    db = client[database]
    col = db[collection]

    cursor=col.find()
    docs=list(cursor)

    #make series to be importable as json

    docs1 = pandas.DataFrame(columns=[])
    for num, doc in enumerate( docs ):
        doc["_id"] = str(doc["_id"])
        doc_id = doc["_id"]
        series_obj = pandas.Series(doc, name=doc_id)
        docs1 = docs1.append(series_obj)

    docs1.to_json(filename)
