# Replace these values with your actual database connection details
import mysql.connector

def chk():
    host = "localhost"
    user = "root"
    password = "shiva"
    database_name = 'switzbank'
    # Connect to the MySQL server
    connection = mysql.connector.connect(host=host, user=user, password=password, database=database_name)
    cursor = connection.cursor()
    try:
        # Execute the SELECT query with placeholders
        cursor.execute('SET SQL_SAFE_UPDATES = 0')
        query = "UPDATE users SET debit_card_pin = %s WHERE debit_card_no = %s AND mobile_no= %s"
        values = ('0000','SWTZ780980KZ','9392953796')
        cursor.execute(query, values)
        connection.commit()
        print('Password updated successfully')
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
chk()