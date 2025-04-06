import psycopg2

def connection():
    try:

        #Internal database host from cloud to cloud 
        conn = psycopg2.connect(user="testdb_pc0s_user",
                            password="CpWMnbHsqZM751EgEjbzHyhGGfXfNmPk",
                            host="dpg-cvndib63jp1c738hnrn0-a",
                            port="5432",
                            database="testdb_pc0s")
 

        
        """# Internal database connection from local to local
        conn = psycopg2.connect(user="postgres",
                                    password="postgres",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="testdb") """
        return conn
          
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return None


            
