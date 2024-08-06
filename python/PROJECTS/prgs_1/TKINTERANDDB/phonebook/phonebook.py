import mysql.connector

class Phone_Book:

    def __init__(self):
        self.host = 'localhost'
        self.username = 'root'
        self.passwd = 'root'
        self.database = 'phonebook'

    def conn(self):
        # Establish a connection to MySQL
        con = mysql.connector.connect(host=self.host, user=self.username, passwd=self.passwd)
        cur = con.cursor()

        try:
            # Create the database if it doesn't exist
            cur.execute(f'CREATE DATABASE IF NOT EXISTS {self.database}')
            print('Successfully created or connected to the database')
        except mysql.connector.Error as err:
            print(f'Failed to create or connect to the database: {err}')
        finally:
            cur.close()
            con.close()

    def login(self):
        pass

    def signup(self):
        pass
    
    def index(self):
        pass

    def get_data(self):
        pass

    def put_data(self):
        pass

# Create an instance of Phone_Book and call the conn method
obj = Phone_Book()
obj.conn()
