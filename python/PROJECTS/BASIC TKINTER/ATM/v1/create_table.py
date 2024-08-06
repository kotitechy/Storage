import pymysql
from db_create import database_exists  # Assuming you have this function defined


def create_users_table():
    connection = pymysql.connect(host="localhost",user='root',password='root',database='switzbank')
    cursor = connection.cursor()

    try:
        create_table_query = '''use switz_bank'''
        cursor.execute('''CREATE TABLE USERS (acc_no INT AUTO_INCREMENT PRIMARY KEY,user_name VARCHAR(80) NOT NULL,dob DATE NOT NULL,gender VARCHAR(10) NOT NULL,address VARCHAR(100) NOT NULL,qualification VARCHAR(20) NOT NULL,mobile_no BIGINT(12) NOT NULL,adhar_no VARCHAR(20) NOT NULL,email VARCHAR(50) NOT NULL,acc_type VARCHAR(7) NOT NULL,amount DECIMAL(9,2),debit_card_no VARCHAR(16),debit_card_pin INT(6),prof_img LONGBLOB,id_proof LONGBLOB,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)AUTO_INCREMENT = 780980;''')
        connection.commit()
        print('Created table USERS successfully')
    except:
        print('Table USERS already exists')

def create_authen_table():
    connection = pymysql.connect(host="localhost",user='root',password='root',database='switzbank')
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES LIKE 'authen'")
    table_exists = cursor.fetchall()

    if not table_exists:
        create_table_query1 = "CREATE TABLE authen (sno int,atm_no VARCHAR(40),pass VARCHAR(10))"
        cursor.execute(create_table_query1)
        print('Created table authen successfully')
        create_sam_data = "INSERT INTO authen (sno,atm_no, pass) VALUES(1,' ', ' ');"
        connection.commit()
        cursor.execute(create_sam_data)
        print('Data successfully updated')
    else:
        print('Table authen already exists')

def close_connection(cursor, connection):
    if cursor:
        cursor.close()
    if connection:
        connection.close()

create_users_table()
create_authen_table()