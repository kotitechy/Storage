from os.path import exists
import mysql.connector

# Replace these values with your actual database connection details
host = "localhost"
user = "root"
password = "shiva"
database_name = 'switzbank'

# Connect to the MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

try:
    # Check if the database exists
    cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
    database_exists = cursor.fetchone()

    if not database_exists:
        # Create the database if it doesn't exist
        create_database_query = f"CREATE DATABASE {database_name}"
        cursor.execute(create_database_query)
        print(f"Database '{database_name}' created successfully.")
    else:
        print(f"Database '{database_name}' already exists. Skipping creation.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
    print('Failed to create or check the database.')

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
