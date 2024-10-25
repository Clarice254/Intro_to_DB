import mysql.connector
from mysql.connector import errorcode

def create_database():
    # Define the database name
    database_name = "alx_book_store"
    
    # Validate database name is not empty
    if not database_name.strip():
        print("Error: Database name cannot be empty.")
        return
    
    # Connect to the MySQL server
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",     # Replace with your MySQL username
            password="1372Clara"  # Replace with your MySQL password, ensuring no leading/trailing spaces
        )
        cursor = conn.cursor()
        
        # Attempt to create the database
        try:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
            print(f"Database '{database_name}' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed to create database '{database_name}': {err}")
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Check your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Connection failed: {err}")
    finally:
        # Close the cursor and connection
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    create_database()
