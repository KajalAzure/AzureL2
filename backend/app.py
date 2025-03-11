from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Create database table
def create_table():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL)''')
    conn.commit()
    conn.close()

# Add sample products
def insert_sample_data():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES ('Laptop', 899.99)")
    cursor.execute("INSERT INTO products (name, price) VALUES ('Smartphone', 499.99)")
    cursor.execute("INSERT INTO products (name, price) VALUES ('Headphones', 99.99)")
    conn.commit()
    conn.close()

# API Endpoint to Get Products
@app.route('/products', methods=['GET'])
def get_products():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return jsonify(products)

# API Endpoint to Add Product
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    price = data['price']
    
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    conn.close()
    return jsonify({"message": "Product added successfully!"})

if __name__ == '__main__':
    create_table()
    insert_sample_data()
    app.run(debug=True)
