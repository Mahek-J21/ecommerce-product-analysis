# E-commerce Product Analysis Using MongoDB

## Project Overview

This project analyzes e-commerce data using **MongoDB, Python, and Streamlit**. It uses product, order, order item, and review data to identify sales trends, explore product categories, analyze order statuses, and understand customer review scores.

The project demonstrates how NoSQL databases and data visualization tools can be used to extract meaningful insights from e-commerce datasets.

## Objectives

- Store and manage e-commerce data using MongoDB.
- Perform data analysis using MongoDB aggregation pipelines.
- Analyze product categories and sales performance.
- Examine order statuses and customer review scores.
- Build an interactive dashboard using Streamlit.
- Connect Python applications to MongoDB using PyMongo.

## Technologies Used

- **Python 3.11** – Data processing and application development
- **MongoDB Community Server** – NoSQL database
- **MongoDB Compass** – Database management and aggregation analysis
- **PyMongo** – Python integration with MongoDB
- **Pandas** – Data manipulation
- **Streamlit** – Interactive dashboard development
- **Plotly / Streamlit charts** – Data visualization, where used

## Dataset

The project uses the Brazilian E-Commerce Public Dataset by Olist.

The dataset contains information about products, orders, order items, and customer reviews.

The following collections are used in MongoDB:

| Collection | Description |
|---|---|
| `products` | Product details and category information |
| `order_items` | Products purchased in individual orders, including item prices |
| `orders` | Order information and order statuses |
| `reviews` | Customer review information and scores |

Dataset source: [Brazilian E-Commerce Public Dataset by Olist on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

**Note:** Download the dataset separately. Dataset files are excluded from this repository.

## Key Features

### 1. Product Category Analysis
Analyzes the number of products in different categories.

### 2. Sales Analysis
Calculates product-level sales values and identifies top-performing products.

### 3. Category Sales Analysis
Uses MongoDB aggregation and `$lookup` to combine product and order-item information and calculate sales by category.

### 4. Order Status Analysis
Examines the distribution of orders by status.

### 5. Customer Review Analysis
Calculates the average customer review score.

### 6. Interactive Dashboard
Displays key metrics, tables, and charts through a Streamlit web application.

## Project Structure

```text
Ecommerce-Product-Analysis/
├── dashboard.py
├── ecommerce_analysis.py
├── test_mongodb.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### Prerequisites

Install the following:

- Python 3.11 or a compatible Python version
- MongoDB Community Server
- MongoDB Compass
- Git (optional, for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/ecommerce-product-analysis.git
cd ecommerce-product-analysis
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 3: Start MongoDB

Ensure your local MongoDB server is running.

The Python scripts use this local connection string:

```text
mongodb://localhost:27017
```

### Step 4: Import the Dataset

1. Open MongoDB Compass.
2. Connect to `mongodb://localhost:27017`.
3. Create or select the database `ecommerce_analysis`.
4. Import the corresponding dataset CSV files into the collections:
   - `products`
   - `order_items`
   - `orders`
   - `reviews`

Ensure the collection names and field names match those expected by the Python scripts.

### Step 5: Test the MongoDB Connection

```bash
python test_mongodb.py
```

### Step 6: Run the Analysis Script

```bash
python ecommerce_analysis.py
```

### Step 7: Launch the Dashboard

```bash
streamlit run dashboard.py
```

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

## Example Results

The dashboard and aggregation pipelines can be used to explore metrics such as:

- Total products: 32,951
- Total order items: 112,650
- Total orders: 99,441
- Average review score: approximately 4.09 out of 5

These figures reflect the dataset imported for this project. Results may vary if different data or filters are used.

**Important:** Sales values calculated from order-item prices represent the sum of listed item prices, not profit or net revenue. They do not necessarily account for freight, discounts, refunds, or other costs.

## MongoDB Concepts Demonstrated

- Database and collection management
- Document queries and filtering
- Aggregation pipelines
- `$match`, `$group`, `$sort`, and `$lookup`
- Indexing to improve query performance
- Joining related data across collections

## Future Enhancements

- Add interactive filters for product categories and order dates.
- Include geographic sales analysis.
- Analyze delivery performance and customer satisfaction.
- Add more visualizations and downloadable reports.
- Deploy the Streamlit dashboard online.

## Author

**Student Project**  
E-commerce Product Analysis Using MongoDB, Python, and Streamlit

## License

This project is intended for educational and academic purposes. Refer to the original dataset's terms on Kaggle for dataset usage conditions.
