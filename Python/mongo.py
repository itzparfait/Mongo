from pymongo import MongoClient

# Connect to MongoDB (running in Docker on localhost)
client = MongoClient("mongodb://localhost:27017/")

# Step 1: Create a database named "my_database"
db = client["mongo-database"]

# Step 2: Create a collection named "my_collection"
collection = db["my_collection"]

# Step 3: Insert a sample document
sample_document = {
    "name": "Parfait",
    "value": 20
}
insert_result = collection.insert_one(sample_document)
print("Inserted document ID:", insert_result.inserted_id)

# Step 4: List all databases and check if "my_database" exists
print("\nAvailable databases:")
db_list = client.list_database_names()
for database in db_list:
    print("-", database)

if "mongo-database" in db_list:
    print("\n✅ 'mongo-database' exists!")
else:
    print("\n❌ 'mongo-database' not found.")
