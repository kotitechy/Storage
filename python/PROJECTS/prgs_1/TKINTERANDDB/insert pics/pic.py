import sqlite3

db= sqlite3.connect('ellenki.db')
cr = db.cursor()

cr.execute('create table if not exists students(id auto increment,profile blob)')
db.commit()

pc = input('enter an file name : ')
with open(pc,'rb') as image_file:
    image_binary = image_file.read()
    print(image_binary)

cr.execute('insert into students(profile) values (?)',(sqlite3.Binary(image_binary),))
print('pic inserted')
db.commit()
db.close()