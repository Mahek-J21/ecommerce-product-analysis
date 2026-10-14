from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["ecommerce_analysis"]

print("=== E-commerce Product Analysis ===")

# 1. Total products
total_products = db.products.count_documents({})
print("Total products:", total_products)

# 2. Total order items
total_items = db.order_items.count_documents({})
print("Total order items:", total_items)

# 3. Average review score
review_result = list(db.reviews.aggregate([
    {
        "$group": {
            "_id": None,
            "average_score": {"$avg": "$review_score"},
            "total_reviews": {"$sum": 1}
        }
    }
]))

if review_result:
    print("Total reviews:", review_result[0]["total_reviews"])
    print("Average review score:", round(review_result[0]["average_score"], 2))

# 4. Orders by status
print("\nOrders by status:")
for result in db.orders.aggregate([
    {"$group": {"_id": "$order_status", "total": {"$sum": 1}}},
    {"$sort": {"total": -1}}
]):
    print(result["_id"], ":", result["total"])

client.close()