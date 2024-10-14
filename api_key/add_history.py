host='192.168.56.1'
user='admin'
passwd='11971197'
database='chatbot_ai'

import pymysql as sql

def add_query(prompt,username):
    con = None
    try:    
        con = sql.connect(host=host, user=user, passwd=passwd, database=database)
        print('Connection was successful')
        
        cur = con.cursor()
        query = "INSERT INTO queries (query, username) VALUES (%s, %s)"
        cur.execute(query, (prompt, username))
        con.commit()
        # print("Data insertion successful")
        
    except Exception as e:
        print("Data insertion failed:", e)
        
    finally:
        if con:
            con.close()
            print("Connection closed")

# print(con())


