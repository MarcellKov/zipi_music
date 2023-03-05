from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["database"]
collection=db["palotas"]

def insertion(name,age):
    collection.insert_one({"name":name,"age":age})
    print("SUCCESFUL WRITE OPERATION")

def keres(name):
    x=collection.find_one({"name":name})
    #print age of the json object(dict or hashmap in python) we just queried from MongoDB
    print(x["age"])

#beszur("Pal",1680)
keres("Pal")