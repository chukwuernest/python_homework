import sqlite3
import pandas as pd
import numpy as np
import os  


with sqlite3.connect("../db/magazines.db") as conn:
    print("Database created successfully...")

    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    def create_tables(cursor):
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(id)
        );
        """)

    def add_publisher(cursor, name):
        try:
            cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        except sqlite3.IntegrityError:
            print(f"Publisher '{name}' already exists.")

    def add_magazine(cursor, name, publisher_name):
        cursor.execute("SELECT id FROM publishers WHERE name = ?", (publisher_name,))
        result = cursor.fetchone()
        if result:
            publisher_id = result[0]
            try:
                cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
            except sqlite3.IntegrityError:
                print(f"Magazine '{name}' already exists.")
        else:
            print(f"Publisher '{publisher_name}' not found.")

    def add_subscriber(cursor, name, address):
        cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (name, address))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
        else:
            print(f"Subscriber '{name} - {address}' already exists.")

    def add_subscription(cursor, subscriber_name, subscriber_address, magazine_name, expiration_date):
        cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (subscriber_name, subscriber_address))
        sub_result = cursor.fetchone()

        cursor.execute("SELECT id FROM magazines WHERE name = ?", (magazine_name,))
        mag_result = cursor.fetchone()

        if sub_result and mag_result:
            subscriber_id = sub_result[0]
            magazine_id = mag_result[0]
            try:
                cursor.execute("""
                    INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
                    VALUES (?, ?, ?)
                """, (subscriber_id, magazine_id, expiration_date))
            except sqlite3.IntegrityError:
                print("Duplicate subscription not allowed.")
        else:
            print(f"Invalid subscription info for '{subscriber_name}' and '{magazine_name}'.")

    create_tables(cursor)

    add_publisher(cursor, "NaturePub")
    add_publisher(cursor, "TechWorld")
    add_publisher(cursor, "DailyScience")

    add_magazine(cursor, "Nature Monthly", "NaturePub")
    add_magazine(cursor, "Tech Times", "TechWorld")
    add_magazine(cursor, "Science Daily", "DailyScience")

    add_subscriber(cursor, "Alice Johnson", "123 Maple St")
    add_subscriber(cursor, "Bob Smith", "456 Oak Ave")
    add_subscriber(cursor, "Charlie Lee", "789 Pine Dr")

    add_subscription(cursor, "Alice Johnson", "123 Maple St", "Nature Monthly", "2025-12-01")
    add_subscription(cursor, "Bob Smith", "456 Oak Ave", "Tech Times", "2025-11-01")
    add_subscription(cursor, "Charlie Lee", "789 Pine Dr", "Science Daily", "2025-10-01")

    conn.commit()

    print("\n--- All Subscribers ---")
    cursor.execute("SELECT * FROM subscribers;")
    for row in cursor.fetchall():
        print(row)

    print("\n--- All Magazines Sorted by Name ---")
    cursor.execute("SELECT * FROM magazines ORDER BY name ASC;")
    for row in cursor.fetchall():
        print(row)

    print("\n--- Magazines for Publisher 'NaturePub' ---")
    cursor.execute("""
        SELECT magazines.id, magazines.name, publishers.name AS publisher_name
        FROM magazines
        JOIN publishers ON magazines.publisher_id = publishers.id
        WHERE publishers.name = ?
        ORDER BY magazines.name;
    """, ("NaturePub",))
    for row in cursor.fetchall():
        print(row)


lesson_db_path = "../db/lesson.db"
os.makedirs("../db", exist_ok=True)  

with sqlite3.connect(lesson_db_path) as lesson_conn:
    lesson_cursor = lesson_conn.cursor()

    lesson_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    existing_tables = set(row[0] for row in lesson_cursor.fetchall())

    if "products" not in existing_tables:
        lesson_cursor.execute("""
            CREATE TABLE products (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT NOT NULL,
                price REAL NOT NULL
            );
        """)
        lesson_cursor.executemany("""
            INSERT INTO products (product_id, product_name, price)
            VALUES (?, ?, ?);
        """, [
            (1, 'Widget A', 10.0),
            (2, 'Widget B', 15.5),
            (3, 'Widget C', 7.25)
        ])
        print("Created and populated 'products' table.")

    if "line_items" not in existing_tables:
        lesson_cursor.execute("""
            CREATE TABLE line_items (
                line_item_id INTEGER PRIMARY KEY,
                product_id INTEGER,
                quantity INTEGER,
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            );
        """)
        lesson_cursor.executemany("""
            INSERT INTO line_items (line_item_id, product_id, quantity)
            VALUES (?, ?, ?);
        """, [
            (1, 1, 5),
            (2, 2, 2),
            (3, 3, 10),
            (4, 1, 3)
        ])
        print("Created and populated 'line_items' table.")

    lesson_conn.commit()



print("\n\n=== Pandas Summary from lesson.db ===")

lesson_conn = sqlite3.connect(lesson_db_path)

query = """
    SELECT 
        line_items.line_item_id,
        line_items.quantity,
        line_items.product_id,
        products.product_name,
        products.price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id;
"""

df = pd.read_sql_query(query, lesson_conn)

print("\nFirst 5 rows of the merged DataFrame:")
print(df.head())

df['total'] = df['quantity'] * df['price']

print("\nFirst 5 rows with total column:")
print(df.head())

summary = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
}).rename(columns={'line_item_id': 'order_count', 'total': 'total_sales'})

summary = summary.sort_values(by='product_name')

print("\nGrouped and Sorted Summary:")
print(summary.head())

summary.to_csv("order_summary.csv")
print("\nSummary written to 'order_summary.csv'")

lesson_conn.close()