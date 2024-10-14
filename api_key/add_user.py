host='192.168.56.1'
user='admin'
passwd='11971197'
databse='chatbot_ai'

import pymysql as sql
def con():
    try:
        con=sql.connect(host=host,user=user,passwd=passwd,database=databse)
        print('Connection was sucessfull')
        cur=con.cursor()
        return con,cur
    except Exception as e:
        print(e)


def add_user(username,email):
    try:
        conn,curs=con()
        print("adding user")
        try:
            query=f"insert into users (username,email) values(%s,%s);"
            data=(username,email)
            curs.execute(query,data)
            conn.commit()
            print("Sucessfully created user")
        except Exception as e:
            if (e.args[0] == 1602):
                print("User already exists Try with different one")
    except Exception as e:
        print(e)

add_user("vamshi","k@gmail.com")

