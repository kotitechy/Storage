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
# Connect to a dynamic database
try:
    cur.execute('USE ellenki_college')
    print('Connected to database')
except pymysql.Error as e:
    print(f'Failed to connect to database: {e}')


print('Fetching Data')
# Fetch data
cur.execute(f'SELECT * FROM stu_regs')
result = cur.fetchall()
for i in result:
    print(i)