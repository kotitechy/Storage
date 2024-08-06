import pymysql as sq

u1 = 'rama'
u2 = 'shiva'

db = sq.connect(host='localhost', user='root', passwd='root', database='chatapp')
cur = db.cursor()

cur.execute('select msg, tim from chat where user = "shiva"')
ls = []
r = cur.fetchall()
for i in r:
    print('\t\t\t\t\t\t\trama :' ,i)
    ls.append(i)


cur.execute('select msg, tim from chat where user = "rama"')
r = cur.fetchall()
for j in r:
    print('shiva : ', j)