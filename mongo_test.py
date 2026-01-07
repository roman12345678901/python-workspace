from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['test_database']
collection = db['users']

user_data = {"name": "Alice", "age": 30, "city": "New York", "likes": ["cs2", "fifa", "valorant"]}

insert_result = collection.insert_one(user_data)

print ("Inserted document ID:", insert_result.inserted_id)

found_user = collection.find_one({"name": "Alice"})

print ("Found user:", found_user)