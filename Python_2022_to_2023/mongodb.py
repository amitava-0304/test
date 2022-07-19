import pymongo
client = pymongo.MongoClient("mongodb+srv://amitava_2112:Suman123@python.e0zfy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
d1 = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
print(client.list_database_names())
