import mysql.connector
from db_create import database_exists  # Assuming you have this function defined

def initialize_database(host, user, password, database_name='switzbank'):
    connection = None
    cursor = None

    try:
        # Connect to the database
        connection, cursor = connect_to_database(host, user, password)

        # Create the database if it doesn't exist
        create_database_if_not_exists(cursor, database_name)

        # Create the USERS table
        create_users_table(cursor, database_name)

        # Create the authen table
        create_authen_table(cursor)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        close_connection(cursor, connection)

def connect_to_database(host, user, password):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    cursor = connection.cursor()
    return connection, cursor

def create_database_if_not_exists(cursor, database_name):
    if not database_exists():
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' created successfully ")

def create_users_table(cursor, database_name):
    cursor.execute(f'USE {database_name}')
    cursor.execute("SHOW TABLES LIKE 'USERS'")
    table_exists = cursor.fetchall()

    if not table_exists:
        create_table_query = '''CREATE TABLE USERS (acc_no INT AUTO_INCREMENT PRIMARY KEY, ... )'''
        cursor.execute(create_table_query)
        print('Created table USERS successfully')
    else:
        print('Table USERS already exists')

def create_authen_table(cursor):
    cursor.execute("SHOW TABLES LIKE 'authen'")
    table_exists = cursor.fetchall()

    if not table_exists:
        create_table_query1 = "CREATE TABLE authen (sno int,atm_no VARCHAR(40),pass VARCHAR(10))"
        cursor.execute(create_table_query1)
        print('Created table authen successfully')
        create_sam_data = "INSERT INTO authen (sno,atm_no, pass) VALUES(1,' ', ' ');"
        cursor.execute(create_sam_data)
        print('Data successfully updated')
    else:
        print('Table authen already exists')

def close_connection(cursor, connection):
    if cursor:
        cursor.close()
    if connection:
        connection.close()

if __name__ == "__main__":
    # Replace these values with your actual database connection details
    host = "localhost"
    user = "root"
    password = "shiva"

    # Initialize the database
    initialize_database(host, user, password)
