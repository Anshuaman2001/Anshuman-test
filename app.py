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
        c.execute('''
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                image TEXT,
                department TEXT
            )
        ''')
        # Sample data with departments
        c.execute("INSERT INTO products (name, description, price, image, department) VALUES ('Apple', 'Fresh red apple', 0.99, 'apple.jpg', 'Fruits')")
        c.execute("INSERT INTO products (name, description, price, image, department) VALUES ('Banana', 'Ripe yellow banana', 0.49, 'banana.jpg', 'Fruits')")
        c.execute("INSERT INTO products (name, description, price, image, department) VALUES ('Orange', 'Juicy orange', 0.79, 'orange.jpg', 'Fruits')")
        c.execute("INSERT INTO products (name, description, price, image, department) VALUES ('Shampoo', 'Hair care product', 5.49, 'shampoo.jpg', 'Personal Care')")
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
            'image': row[4],
            'department': row[5]
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
        SET name = ?, description = ?, price = ?, image = ?, department = ?
        WHERE id = ?
    ''', (data['name'], data['description'], data['price'], data['image'], data['department'], product_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product updated successfully'})

@app.route('/api/departments', methods=['GET'])
def get_departments():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT DISTINCT department FROM products")
    departments = [{'department': row[0]} for row in c.fetchall()]
    conn.close()
    return jsonify(departments)

@app.route('/api/departments/<department_name>/products', methods=['GET'])
def get_products_by_department(department_name):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE department = ?", (department_name,))
    products = [
        {
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'price': row[3],
            'image': row[4],
            'department': row[5]
        }
        for row in c.fetchall()
    ]
    conn.close()
    return jsonify(products)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
