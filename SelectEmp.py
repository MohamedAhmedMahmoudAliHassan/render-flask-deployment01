import psycopg2


def select_emp():
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
        
        
        cur = connection.cursor()
        cur.execute("SELECT * FROM employee;") # Replace with your SQL query
        data = cur.fetchall()
        # Get column names
        column_names = [desc[0] for desc in cur.description]
        cur.close()
        connection.close()
        return data, column_names  # Return both data and column names
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return []