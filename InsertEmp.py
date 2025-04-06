import psycopg2
from db_connection import connection


def insert_to_table(personal_number, employee_name):
    try:
        conn = connection()
        cursor = conn.cursor()

        postgres_insert_query = """ INSERT INTO employee (personal_number, name) VALUES (%s,%s)"""
        record_to_insert = (personal_number, employee_name)
        cursor.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
            
