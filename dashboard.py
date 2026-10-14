import streamlit as st
import pandas as pd
from pymongo import MongoClient

st.set_page_config(
    page_title="E-commerce Product Analysis",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 E-commerce Product Analysis")
st.caption("MongoDB-powered analysis of the Olist e-commerce dataset")

@st.cache_resource
def get_database():
    client = MongoClient(
        "mongodb://localhost:27017",
        serverSelectionTimeoutMS=5000
    )
    client.admin.command("ping")
    return client["ecommerce_analysis"]

try:
    db = get_database()

    # Key metrics
    total_products = db.products.count_documents({})
    total_items = db.order_items.count_documents({})
    total_orders = db.orders.count_documents({})

    review_data = list(db.reviews.aggregate([
        {"$group": {
            "_id": None,
            "average_score": {"$avg": "$review_score"},
            "total_reviews": {"$sum": 1}
        }}
    ]))

    average_score = (
        round(review_data[0]["average_score"], 2)
        if review_data and review_data[0]["average_score"] is not None
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Products", f"{total_products:,}")
    col2.metric("Order Items", f"{total_items:,}")
    col3.metric("Total Orders", f"{total_orders:,}")
    col4.metric("Average Review Score", f"{average_score}/5")

    st.divider()

    # Orders by status
    st.subheader("📦 Orders by Status")

    status_data = list(db.orders.aggregate([
        {"$group": {
            "_id": "$order_status",
            "total": {"$sum": 1}
        }},
        {"$sort": {"total": -1}}
    ]))

    if status_data:
        status_df = pd.DataFrame(status_data).rename(
            columns={"_id": "Order Status", "total": "Orders"}
        )
        status_df = status_df.set_index("Order Status")
        st.bar_chart(status_df, horizontal=True)
        st.dataframe(status_df, use_container_width=True)

    st.divider()

    # Top 10 categories by product count
    st.subheader("🏷️ Top 10 Product Categories by Product Count")

    category_data = list(db.products.aggregate([
        {"$match": {"product_category_name": {"$ne": None}}},
        {"$group": {
            "_id": "$product_category_name",
            "total_products": {"$sum": 1}
        }},
        {"$sort": {"total_products": -1}},
        {"$limit": 10}
    ]))

    if category_data:
        category_df = pd.DataFrame(category_data).rename(
            columns={
                "_id": "Category",
                "total_products": "Products"
            }
        )
        st.bar_chart(
            category_df.set_index("Category"),
            horizontal=True
        )
        st.dataframe(category_df, use_container_width=True)

    st.divider()

    # Top 10 products by item-price value
    st.subheader("💰 Top 10 Products by Item-Price Value")

    sales_data = list(db.order_items.aggregate([
        {"$group": {
            "_id": "$product_id",
            "total_sales": {"$sum": "$price"},
            "times_ordered": {"$sum": 1}
        }},
        {"$sort": {"total_sales": -1}},
        {"$limit": 10}
    ]))

    if sales_data:
        sales_df = pd.DataFrame(sales_data).rename(
            columns={
                "_id": "Product ID",
                "total_sales": "Item-Price Value",
                "times_ordered": "Order Item Records"
            }
        )
        sales_df["Item-Price Value"] = sales_df["Item-Price Value"].round(2)
        st.dataframe(sales_df, use_container_width=True)
    else:
        st.info("No sales data was found.")

except Exception as e:
    st.error("Could not load the dashboard data.")
    st.code(str(e))

st.caption("Local MongoDB • Olist dataset • E-commerce analytics")