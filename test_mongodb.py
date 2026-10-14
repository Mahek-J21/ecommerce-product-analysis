from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=5000)

try:
    client.admin.command("ping")
    print("MongoDB connection successful!")

    db = client["ecommerce_analysis"]
    print("Collections:", db.list_collection_names())

except Exception as e:
    print("Connection error:", e)

finally:
    client.close()