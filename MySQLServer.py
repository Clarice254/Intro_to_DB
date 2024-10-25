import mysql.connector
from mysql.connector import errorcode

def create_database():
    database_name = "alx_book_store"

    if not database_name.strip():
        print("Error: Database name cannot be empty.")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1372Clara"
        )
        cursor = conn.cursor()

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
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    create_database()
