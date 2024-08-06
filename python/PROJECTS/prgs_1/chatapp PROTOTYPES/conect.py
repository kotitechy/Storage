import pymysql as ps

database = 'database-2'
user = 'admin'
password = 'admin123'
port = '3306'
host = 'database-2.cnu8u8is2p4e.us-east-1.rds.amazonaws.com'

try:
    db = ps.connect(host='localhost',user='root',passwd='root')
    cur = db.cursor()
    print('Connected to db')
    try:
        cur.execute('show databases')
        r = cur.fetchall()
        print('databases are : ',r)
    except:
        print('failed to load data from db')
    

except ps.connector.Error as e:
    print("Unable to connect to the database:", e)
