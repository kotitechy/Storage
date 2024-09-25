import pymysql as sq
import os

try:
    con = sq.connect(
        host="database-mysql.c9iwyuqw83oz.eu-north-1.rds.amazonaws.com",
        user="admin",
        passwd="11971197",  # Corrected this line
        database="shiva"
    )
    print("Connection successful!")

    with con.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS u2 (sno INT PRIMARY KEY, name VARCHAR(255))")
        print("Table created")
        
        cur.execute("INSERT INTO u2 VALUES (1, 'Shivan')")
        print("Data inserted")
        
        cur.execute("UPDATE u2 SET name = 'Karthik' WHERE sno = 1")
        print("Data updated")
        
        cur.execute("SELECT * FROM u2")
        r = cur.fetchall()
        print("Data:", r)
        
    con.commit()  # Commit changes

except sq.MySQLError as e:
    print("MySQL Error:", e)
except Exception as e:
    print("Error:", e)

finally:
    if 'con' in locals() and con.open:  # Check if con was successfully created before closing
        con.close()
        print("Connection closed.")
