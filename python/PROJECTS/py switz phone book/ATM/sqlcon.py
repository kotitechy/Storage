import pymysql as sql


class sqlc:
    cre = ['localhost', 'root', 'root', 'switzbank']

    # 1
    def db(self):
        try:
            con = sql.connect(host=self.cre[0], user=self.cre[1], passwd=self.cre[2])
            print('connected to db')
            try:
                cur = con.cursor()
                print('created cursor')
                try:
                    # cur.execute('show databases')
                    cur.execute('CREATE DATABASE switzbank')
                    print('CREATED DB')
                except Exception as e:
                    print('failed to execute query', e)
                finally:
                    con.close()
            except Exception as e:
                print('failed to create cursor')
            finally:
                con.close()
        except Exception as e:
            print('failed to connect to db: ', e)

    # 2
    def table(self):
        try:
            con = sql.connect(host=self.cre[0], user=self.cre[1], passwd=self.cre[2], database=self.cre[3])
            print('connected to db')
            try:
                cur = con.cursor()
                print('created cursor')
                try:
                    sqlq = """CREATE TABLE USER (acc_no INT AUTO_INCREMENT,PRIMARY KEY (acc_no),user_name VARCHAR(80) 
                    NOT NULL,dob DATE NOT NULL,gender VARCHAR(10) NOT NULL,address VARCHAR(100) NOT NULL,
                    qualification VARCHAR(20) NOT NULL,mobile_no BIGINT(12) NOT NULL,adhar_no VARCHAR(20) NOT NULL,
                    email VARCHAR(50) NOT NULL,acc_type VARCHAR(7) NOT NULL,amount DECIMAL(9,2),debit_card_no 
                    VARCHAR(16),debit_card_pin INT(6),prof_img LONGBLOB,id_proof LONGBLOB,created_at TIMESTAMP 
                    DEFAULT CURRENT_TIMESTAMP,updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE 
                    CURRENT_TIMESTAMP)"""
                    cur.execute(sqlq)
                    print('CREATED TABLE')
                except Exception as e:
                    print('failed to execute query', e)
                finally:
                    con.close()
            except Exception as e:
                print('failed to create cursor')
            finally:
                con.close()
        except Exception as e:
            print('failed to connect to db: ', e)

    # 3
    def connection(self):
        try:
            con = sql.connect(host='localhost', user='root', passwd='root', database=self.cre[3])
            print('connected to db')
            try:
                cur = con.cursor()
                print('created cursor')
                return cur, con
            except Exception as e:
                print('failed to create cursor')

        except Exception as e:
            print('failed to connect to db')

    # 3
    def register(self, user_name, dob, gender, address, qualification, mobile_number, adhar_number, email, account_type,
                 prof_data, id_data):
        try:

            import datetime
            try:
                # con = sql.connect(host='localhost', user='root', passwd='root', database='switzbank')
                import sqlite3 as sq
                try:
                    con = sq.connect('switzbank.db')
                    print('connected to db')
                
                    cur = con.cursor()
                    print('created cursor')
                    # return cur, con
                    # Assuming date_str is '04/04/2005'
                    dobs = datetime.datetime.strptime(dob, '%m/%d/%Y')
                    formatted_date = dobs.strftime('%Y-%m-%d')

                    # Execute the INSERT query with placeholders
                    query = "INSERT INTO USER (user_name, dob, gender, address, qualification, mobile_no, adhar_no, email, acc_type,prof_img,id_proof) VALUES (%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    values = (
                        user_name, dobs, gender, address, qualification, mobile_number, adhar_number, email,
                        account_type,
                        prof_data, id_data)
                    try:
                        cur.execute(query, values)
                        print('DATA INSERTED SUCCESSFULLY')
                    except Exception as e:
                        print('error', e)
                except sql.Error as err:
                    print(f'FAILED TO INSERT DATA: {err}')
            except Exception as e:
                print('failed to create cursor')

        except Exception as e:
            print('failed to connect to db')


ob = sqlc()
ob.register('shiva', "02/03/2009", 'male', 'osm', 'ssc', 2, 2, 'a@gmail.com', 'minor', '111', '0101')
# ob.table()
