from pymongo import MongoClient

# create a DB connection instance for the database
client = MongoClient('localhost', 37017)

#creating a db
db = client['summer-db']

#creating collection
collection = db['icecreams']

#data example
data_entry = {"brand": "rududu", "weight":25, "cost": 1.25}
data_forwards = {"brand":"nykstuka", "weight":50, "cost": 1.5, "nickname": "small"}

# collection.insert_one(data_entry)
collection.insert_many([data_entry, data_forwards])