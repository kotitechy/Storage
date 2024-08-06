import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="shiva")

cur = db.cursor()

cur.execute("show databases")

for i in cur:
    print(i) 
cur.execute("use shivdb")
# cur.execute("create table dept(id int primary key,name varchar(20) not null)")
cur.execute("show tables")
print("Tables in db are : ")
for j in cur:
    print(j)
print("Values in the table are :")

cur.execute("select * from student")

result = cur.fetchall()
for i in result:
    print(i)

print("Values in the table are :")

cur.execute("select * from student")

result = cur.fetchall()
for i in result:
    print(i)
print("only one :")

cur.execute("select * from student")

result = cur.fetchone()
for i in result:
    print(i)