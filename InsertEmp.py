import psycopg2


def insert_to_table():
    try:
        '''
        #Internal database host from cloud to cloud 
        connection = psycopg2.connect(user="testdb_pc0s_user",
                            password="CpWMnbHsqZM751EgEjbzHyhGGfXfNmPk",
                            host="dpg-cvndib63jp1c738hnrn0-a",
                            port="5432",
                            database="testdb_pc0s")
        '''

    
        # Internal database connection from local to local
        connection = psycopg2.connect(user="postgres",
                                    password="postgres",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="testdb")

        
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO employee (personal_number, name) VALUES (%s,%s)"""
        record_to_insert = ('emp003', 'Mahmoud Seddik')
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
            
insert_to_table()