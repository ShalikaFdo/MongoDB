import json
import pymongo

from pymongo import MongoClient
client = MongoClient()

db=client.school
collection=db.student_collection
page=open("test.json",'r')
dataset=json.loads(page.read())

for item in dataset:
    collection.insert(item)

for item in collection.find():
    print(item)
print("\n")    

print("Document with _id=56d109c30ba6cfc76142cffe\n")    
for item in collection.find({"_id":"56d109c30ba6cfc76142cffe"}):
    print(item)
print("\n")

print("Balances in ascending order\n")
for item in collection.find().sort("balance", pymongo.ASCENDING):
    print(item["balance"])
