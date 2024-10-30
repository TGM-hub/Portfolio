import mysql.connector
from mysql.connector import Error

# Database configuration
DB_CONFIG = {
    'host': '192.168.1.24',       
    'user': 'TGM',
    'password': '18072202Tt!',
    'database': 'nutrition_db'
}

# Function to create and return a database connection
def create_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except Error as e:
        print(f"Error connecting to MariaDB: {e}")
        return None