import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    c = conn.cursor()



import sqlite3
import pandas as pd
import numpy as np
import os


conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

conn.execute("PRAGMA foreign_keys = ON;")


cursor.execute("DROP TABLE IF EXISTS line_items;")
cursor.execute("DROP TABLE IF EXISTS orders;")
cursor.execute("DROP TABLE IF EXISTS products;")
cursor.execute("DROP TABLE IF EXISTS customers;")
cursor.execute("DROP TABLE IF EXISTS employees;")  


cursor.execute("""
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    );
""")

cursor.execute("""   
    CREATE TABLE employees (
        employee_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        employee_id INTEGER,  --  Added employee_id as a foreign key
        FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY(employee_id) REFERENCES employees(employee_id)
    );
""")

cursor.execute("""
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        price REAL
    );
""")

cursor.execute("""
    CREATE TABLE line_items (
        line_item_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        FOREIGN KEY(order_id) REFERENCES orders(order_id),
        FOREIGN KEY(product_id) REFERENCES products(product_id)
    );
""")


cursor.executemany("INSERT INTO customers (customer_id, customer_name) VALUES (?, ?)", [
    (1, 'Alice'),
    (2, 'Bob'),
    (3, 'Charlie'),
    (4, 'Perez and Sons')  
])

cursor.executemany("INSERT INTO employees (employee_id, first_name, last_name) VALUES (?, ?, ?)", [
    (1, 'Miranda', 'Harris'), 
    (2, 'John', 'Doe')
])

cursor.executemany("INSERT INTO orders (order_id, customer_id, employee_id) VALUES (?, ?, ?)", [
    (1, 1, 1),
    (2, 2, 2),
    (3, 1, 1),
    (4, 3, 2),
    (5, 1, 1)
])

cursor.executemany("INSERT INTO products (product_id, product_name, price) VALUES (?, ?, ?)", [
    (1, 'Widget A', 10.0),
    (2, 'Widget B', 20.0),
    (3, 'Widget C', 15.5),
    (4, 'Widget D', 5.0),    
    (5, 'Widget E', 8.0),
    (6, 'Widget F', 7.5)
])

cursor.executemany("INSERT INTO line_items (line_item_id, order_id, product_id, quantity) VALUES (?, ?, ?, ?)", [
    (1, 1, 1, 2),
    (2, 1, 2, 1),
    (3, 2, 3, 3),
    (4, 3, 2, 1),
    (5, 4, 1, 4),
    (6, 5, 3, 2)
])

conn.commit()

 #Task 1 
print("\n=== Task 1: Total Price of First 5 Orders ===")
query1 = """
SELECT 
    o.order_id,
    SUM(li.quantity * p.price) AS total_price
FROM orders o
JOIN line_items li ON o.order_id = li.order_id
JOIN products p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
"""
cursor.execute(query1)
results1 = cursor.fetchall()
print("Order ID | Total Price")
print("----------------------")
for order_id, total_price in results1:
    print(f"{order_id:<8} | ${total_price:.2f}")

#Task 2 
print("\n=== Task 2: Average Order Price Per Customer ===")
query2 = """
SELECT 
    c.customer_name,
    AVG(order_totals.total_price) AS average_total_price
FROM customers c
LEFT JOIN (
    SELECT 
        o.customer_id AS customer_id_b,
        SUM(li.quantity * p.price) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
) AS order_totals
ON c.customer_id = order_totals.customer_id_b
GROUP BY c.customer_id;
"""
cursor.execute(query2)
results2 = cursor.fetchall()
print("Customer Name   | Average Total Price")
print("-------------------------------------")
for name, avg_price in results2:
    avg_display = f"${avg_price:.2f}" if avg_price is not None else "No Orders"
    print(f"{name:<16} | {avg_display}")



