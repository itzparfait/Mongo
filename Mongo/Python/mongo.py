from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://parfait:password@localhost:27017/")

# 1. Create database
db = client["my_database"]

# 2. Create collection
collection = db["my_collection"]

# 3. Insert a document
sample_doc = {
    "name": "Parfait",
    "age": 20
}
result = collection.insert_one(sample_doc)

# Confirm insertion
if result.acknowledged:
    print(f"Document inserted with ID: {result.inserted_id}")
else:
    print("Document insertion failed.")

# 4. List all databases
print("\nDatabases on this server:")
print(client.list_database_names())

# 5. Check if our database exists
if "my_database" in client.list_database_names():
    print("Database 'my_database' was successfully created!")
else:
    print("Database not found.")

