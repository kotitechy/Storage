import pymysql as ps

def con():
    try:
        db = ps.connect(host='database-2.cnu8u8is2p4e.us-east-1.rds.amazonaws.com',user='admin',passwd='admin123')
        cur = db.cursor()
        print('Connected to db')
        l = [cur,db]
        return l
    except ps.connector.Error as e:
        print("Unable to connect to the database:", e)

class register:
    def coldata(self):
        self.name = input("Enter Your name: ")
        self.age = int(input("Enter Your age: "))
        self.gender = input("Enter Your gender: ")
        self.mobile = int(input("Enter Your mobile: "))
        self.email = input("Enter Your email: ")
        self.about = input("Enter Your about: ")
        self.desc = input("Enter Your desc: ")
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.mobile)
        print(self.email)
        print(self.about)
        print(self.desc)
        

        


    def registers(self):
        try:
            r = con()
            c = r[0]
            db= r[1]
            self.coldata()

            try:
                q = 'INSERT INTO kinter.users (name, age, gender, mobile, email, about, descrp) VALUES  (%s,%s,%s,%s,%s,%s,%s)'
                d = (self.name, self.age, self.gender, self.mobile, self.email, self.about, self.desc) 
                c.execute(q,d)
                db.commit()
                print('Uers created successfully')
            except Exception as e:
                print('Failed to insert data:', e)
        except Exception as e:
            print('Failed to connect to the database:', e)


s1 = register()
s1.registers()
