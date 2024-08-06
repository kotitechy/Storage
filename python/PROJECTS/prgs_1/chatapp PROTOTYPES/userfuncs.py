import sqlite3 as ps

database = 'database-2'
user = 'admin'
password = 'admin123'
port = '3306'
host = 'database-2.cnu8u8is2p4e.us-east-1.rds.amazonaws.com'
def con():
    try:
        db = ps.connect('chatapp.db')
        cur = db.cursor()
        print('Connected to db')
        l = [cur,db]
        return l
    except ps.connector.Error as e:
        print("Unable to connect to the database:", e)

con()    