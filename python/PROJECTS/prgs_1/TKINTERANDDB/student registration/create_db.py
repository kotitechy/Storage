import pymysql

class create_db:
# Create a connection to the MySQL server
    def conn(self):
        try:
            connection = pymysql.connect(host = "localhost",user = "root",password = "shiva")
            print("Connected to MySQL server successfully!")
        except pymysql.Error as e:
            print(f"Could not Connect : {e}")

        #create a database
        try:
            cursor = connection.cursor()
            print("pointer created")
        except pymysql.Error as e:
            print(f"Error: {e}")
        try:
            db_name = input("\n Don't include spaces in between \n Enter Database name to be created  : ")

            # Create the database
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"Database '{db_name}' created successfully!")
        except pymysql.Error as e:
         print(f"Error: {e}")


