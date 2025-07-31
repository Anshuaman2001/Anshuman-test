from flask import Flask, jsonify, abort
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

DB_PATH = "ecommerce.db"

@app.route("/", methods=["GET"])
def home():
    return "Flask API is running!", 200

# Get all products
@app.route("/api/products", methods=["GET"])
def get_products():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()

    products = [
        dict(zip(
            ["id", "cost", "category", "name", "brand", "retail_price", "department", "sku", "distribution_center_id"],
            row
        )) for row in rows
    ]
    return jsonify(products), 200

# Get product by ID
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        product = dict(zip(
            ["id", "cost", "category", "name", "brand", "retail_price", "department", "sku", "distribution_center_id"],
            row
        ))
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
