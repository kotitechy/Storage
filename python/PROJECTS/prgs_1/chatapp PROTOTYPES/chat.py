from userfuncs import con
from datetime import datetime

class chat:

    def crtcht(self):
        l = con()
        c = l[0]
        db = l[1]
        try:
            # c.execute('use kinter')
            # c.execute('CREATE TABLE kinter.chatcache (fromu varchar(255),chat int(255),timesent datetime,tou varchar(255))')
            c.execute('CREATE TABLE IF NOT EXISTS chats (user TEXT, body TEXT, timesent TEXT, tou TEXT);')
            ct = datetime.now()
            print(ct)
            print('created chat table')
            # c.commit()
        except Exception as e:
            print('failed to create users table',e)

c1 = chat()
c1.crtcht()