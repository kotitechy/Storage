from userfuncs import con
def tablecrt():
        c = con()
        try:
            c.execute('use kinter')
            c.execute('CREATE TABLE users (name varchar(255),age int(255),gender varchar(255),mobile int(50) PRIMARY KEY,email varchar(50),about varchar(255),descrp varchar(255))')
            c.commit()
            print('created users table')
        except Exception as e:
            print('failed to create users table',e)