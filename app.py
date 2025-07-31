from flask import Flask, jsonify
from flask_cors import CORS 
import sqlite3
import os

app = Flask(__name__)
CORS(app)
DATABASE = 'database.db'

def init_db():
    # Only create the database if it doesn't exist
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        # Create table
        c.execute('''CREATE TABLE products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL
                    )''')
        # Insert sample data
        c.execute("INSERT INTO products (name, price) VALUES ('Apple', 0.99)")
        c.execute("INSERT INTO products (name, price) VALUES ('Banana', 0.49)")
        c.execute("INSERT INTO products (name, price) VALUES ('Orange', 0.79)")
        conn.commit()
        conn.close()
        print("Database initialized with sample data.")

@app.route('/api/products', methods=['GET'])
def get_products():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = [
        {'id': row[0], 'name': row[1], 'price': row[2]}
        for row in c.fetchall()
    ]
    conn.close()
    return jsonify(products)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
