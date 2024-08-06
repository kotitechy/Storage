from admin_db import database

db1 = database()
try:
    cur, db = db1.con()
    print('connected')
except Exception as e:
    print(e)
class user_ops:
    def register(self):
        cur.execute('insert into users ()')

u1 = user_ops()
u1.insert_data()
