import json
import pymongo

from pymongo import MongoClient
client = MongoClient()

db=client.schooll
collection=db.studentt_collection
page=open("test.json",'r')
dataset=json.loads(page.read())

for item in dataset:
    collection.insert(item)

for item in collection.find():
    print(item)
for item in collection.find({"_id":"56d109c30ba6cfc76142cffe"}):
    print(item)

for item in collection.find().sort("balance", pymongo.ASCENDING):
    print(item["balance"])
