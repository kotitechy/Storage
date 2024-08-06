import sqlite3 as sl


class database:
    host = ''
    passwd = ''
    db = ''
    usr = ''

    def con(self):
        try:
            db = sl.connect('msg.db')
            print('connected to db')
            try:
                cur = db.cursor()
                print('cursor created')
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
        finally:
            return cur, db

    def crt_usr(self):
        try:

            cur, db = self.con()
            cur.execute('CREATE TABLE user (pkey INTEGER primary key AUTO_INCREMENT,name TEXT NOT NULL, email TEXT NOT NULL, phone INTEGER NOT NULL UNIQUE, gender TEXT NOT NULL, dob TEXT NOT NULL, passwd TEXT NOT NULL UNIQUE)')
            print('table created')
        except Exception as e:
            print(e)
        finally:
            print('completed')
            db.commit()
            db.close()

def ins_dat(self, name, email, phone, gender, dob, passwd):
    try:
        cur, db = self.con()
        q = "INSERT INTO users (name, email, phone, gender, dob, passwd) VALUES (%s, %s, %s, %s, %s, %s)"
        dat = (name, email, int(phone), gender, dob, passwd)  # Convert phone to int if necessary
        cur.execute(q, dat)
        print('data inserted')
    except Exception as e:
        print(e)
    finally:
        db.commit()  # Commit changes
        db.close()   # Close connection


db1 = database()
db1.crt_usr()
