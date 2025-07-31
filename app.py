from flask import Flask, request, jsonify
from flask_cors import CORS 
import sqlite3
import os

app = Flask(__name__)
CORS(app)
DATABASE = 'database.db'

def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        # Updated table with description and image columns
        c.execute('''
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                image TEXT
            )
        ''')
        # Insert sample data
        c.execute("INSERT INTO products (name, description, price, image) VALUES ('Apple', 'Fresh red apple', 0.99, 'apple.jpg')")
        c.execute("INSERT INTO products (name, description, price, image) VALUES ('Banana', 'Ripe yellow banana', 0.49, 'banana.jpg')")
        c.execute("INSERT INTO products (name, description, price, image) VALUES ('Orange', 'Juicy orange', 0.79, 'orange.jpg')")
        conn.commit()
        conn.close()
        print("Database initialized with sample data.")

@app.route('/api/products', methods=['GET'])
def get_products():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = [
        {
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'price': row[3],
            'image': row[4]
        }
        for row in c.fetchall()
    ]
    conn.close()
    return jsonify(products)

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute('''
        UPDATE products
        SET name = ?, description = ?, price = ?, image = ?
        WHERE id = ?
    ''', (data['name'], data['description'], data['price'], data['image'], product_id))

    conn.commit()
    conn.close()
    return jsonify({'message': 'Product updated successfully'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
