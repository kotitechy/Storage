host='192.168.56.1'
user='admin'
passwd='11971197'
database='chatbot_ai'

import pymysql as sql

def get_history(username):
    con = None
    try:    
        con = sql.connect(host=host, user=user, passwd=passwd, database=database)
        print('Connection was successful')
        
        cur = con.cursor()
        query = "select query from queries where username=%s;"
        cur.execute(query, username)
        r=cur.fetchall()
        # list of tuples 
        ls=[]
        for i in r:
            for j in i:
                ls.append(j)
        # print(ls)
        return ls
        
    except Exception as e:
        # print("Data insertion failed:", e)
        return "No history Found"
        
    finally:
        if con:
            con.close()
            # print("Connection closed")



get_history("shiva")