import psycopg2


def insert_to_table(form_product_id):
    try:
        connection = psycopg2.connect(user="testdb_pc0s_user",
                                    password="CpWMnbHsqZM751EgEjbzHyhGGfXfNmPk",
                                    host="dpg-cvndib63jp1c738hnrn0-a.oregon-postgres.render.com",
                                    port="5432",
                                    database="testdb_pc0s")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO employee (personal_number, name) VALUES (%s,%s)"""
        product_id =  str(form_product_id)
        record_to_insert = ('emp002', 'Ahmed Mahmoud')
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
insert_to_table(1)