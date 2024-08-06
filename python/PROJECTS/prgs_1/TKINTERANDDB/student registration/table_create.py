import pymysql
class c_table:
    def tab(self):
        # Create a connection to the MySQL server
        try:
            db = pymysql.connect(host = "localhost",user = "root",password = "shiva")
            cr = db.cursor()
            print("Connected to MySQL server successfully!")
        except pymysql.Error as e:
            print(f"Could not Connect : {e}")

        try:
            cr.execute('use ellenki_college')
            print('db connected')
            cr.execute('CREATE TABLE IF NOT EXISTS stu_regs(full_name varchar(30) not null,email varchar(25) not null,passwd varchar(8) not null,id int primary key auto_increment)')
            print('sucess')
        except pymysql.Error as e:
            print('try again')
        db.close()
        print("Connection closed")
