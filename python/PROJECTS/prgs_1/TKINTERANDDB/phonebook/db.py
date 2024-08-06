import mysql.connector

def con():
    cur = None
    db = None
    try:
        db = mysql.connector.connect(host='localhost', user='root', passwd='root')
        cur = db.cursor()
        print('Successfully connected to db')
    except Exception as e:
        print(f'Failed to connect to db: {e}')
    
    return cur, db

def db_c():
    cur, db = con()
    if cur and db:
        try:
            cur.execute(f'CREATE DATABASE phonebook ')
            db.commit()
            print('Successfully created db')
        except Exception as e:
            print(f'Failed to create db: {e}')

def usr_t():
    cur, db = con()
    if cur and db:
        try:
            # Corrected from 'USE DATABASE' to 'USE'
            cur.execute(f'USE phonebook')
            cur.execute(f'CREATE TABLE usr_table (sno int primary key auto_increment, name varchar(50) not null, contact varchar(15) not null)  ')
            db.commit()
            print('Successfully created USR_TABLE')
        except Exception as e:
            print(f'Failed to create USR_TABLE: {e}')

# Example usage:
# Uncomment and use the following lines to test the functions
db_c()
usr_t()
