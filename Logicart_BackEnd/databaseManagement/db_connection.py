import mysql.connector

# Create connection to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Default is blank
    database="logicart_db"
)

# Check if connected
if db.is_connected():
    print("Connected to MySQL database!")
else:
    print("Failed to connect.")