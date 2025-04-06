import psycopg2
from db_connection import connection


def select_emp():
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employee;") # Replace with your SQL query
        data = cursor.fetchall()
        # Get column names
        column_names = [desc[0] for desc in cursor.description]
        cursor.close()
        conn.close()
        return data, column_names  # Return both data and column names
        
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return []