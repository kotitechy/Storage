import pymysql

# Replace these with your MySQL server details
host = "localhost"
user = "root"
password = "shiva"
# Create a connection to the MySQL server
try:
    db = pymysql.connect(host = "localhost",user = "root",password = "shiva")
    cur = db.cursor()
    print("Connected to MySQL server successfully!")
except pymysql.Error as e:
    print(f"Could not Connect : {e}")
#printing hint
print("Choose an option")
print(' 1. Enter Database Manually \n 2. List out Databases ')
#user input 
che = input("Enter an Option : ")
ch = int(che)
if ch == 1:
    db_name = input("Enter Database name : ")
elif ch == 2:
    cur.execute("show databases")
    print("Listing Databases : ")
    for i in cur:
        print(i) 