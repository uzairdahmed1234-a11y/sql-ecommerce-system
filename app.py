


print("🚀 Hello from Termux & GitHub + MySQL!")

import mysql.connector

# ✅ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ecommerce"
)

cursor = conn.cursor()

# ✅ Create sample data only if tables are empty
cursor.execute("SELECT COUNT(*) FROM users")
user_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM products")
product_count = cursor.fetchone()[0]

if user_count == 0:
    cursor.execute("INSERT INTO users (name, email, password) VALUES ('John Doe', 'john@example.com', '12345')")
    cursor.execute("INSERT INTO users (name, email, password) VALUES ('Jane Smith', 'jane@example.com', 'abcde')")
    print("✅ Added sample users!")

if product_count == 0:
    cursor.execute("INSERT INTO products (name, price, stock) VALUES ('Laptop', 999.99, 5)")
    cursor.execute("INSERT INTO products (name, price, stock) VALUES ('Phone', 499.50, 12)")
    print("✅ Added sample products!")

conn.commit()

# ✅ Display all users
print("\n👤 Users:")
cursor.execute("SELECT * FROM users")
for user in cursor.fetchall():
    print(user)

# ✅ Display all products
print("\n🛒 Products:")
cursor.execute("SELECT * FROM products")
for product in cursor.fetchall():
    print(product)

# ✅ Close connection
conn.close()
print("\n✅ Done!")
print("Hello from Termux & GitHub!")
import mysql.connector

# connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ecommerce"
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES;")

print("✅ Tables in your database:")
for table in cursor.fetchall():
    print("-", table[0])

conn.close()


