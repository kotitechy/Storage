import pymysql

# Replace these with your MySQL server details
host = "localhost"
user = "root"
password = "shiva"

# Create a connection to the MySQL server
try:
    db = pymysql.connect(host=host, user=user, password=password)
    cur = db.cursor()
    print("Connected to MySQL server successfully!")
except pymysql.Error as e:
    print(f"Could not connect: {e}")

# Listing databases
cur.execute("SHOW DATABASES")
print("Listing Databases:")
for i in cur:
    print(i)

# Connect to a dynamic database
try:
    db_name = input('Enter Database name: ')
    cur.execute(f'USE {db_name}')
    print(f'Connected to database: {db_name}')
except pymysql.Error as e:
    print(f'Failed to connect to database: {e}')

# Listing tables
cur.execute('SHOW TABLES')
print("Listing Tables:")
for i in cur:
    print(i)

print('Fetching Data')
# Fetch data
table_name = input('Enter a Table Name: ')
cur.execute(f'SELECT * FROM {table_name}')
result = cur.fetchall()
for i in result:
    print(i)
