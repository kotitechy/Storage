import mysql.connector

def connect(host, user, password, database):
    try:
        # Connect to MySQL
        db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Connected to MySQL")

        # Creating a cursor
        cursor = db.cursor()

        # Executing a query
        cursor.execute("SHOW DATABASES")

        # Fetching the result
        result = cursor.fetchall()
        print("Databases:")
        for db_name in result:
            print(db_name[0])

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection if they exist
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

# Call the connect function with appropriate arguments
connect(host='localhost', user='root', password='root', database='Hotel')
