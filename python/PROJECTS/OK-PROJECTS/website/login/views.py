from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="root",database='chatapp')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="usrname":
                em=value
            if key == 'phno':
                telno = value
            if key=="pass":
                pwd=value
        
        # c="select * from users where email='{}' and password='{}'".format(em,pwd)
        # cursor.execute(c)
        print(em , telno , pwd)
        
        t=tuple(cursor.fetchall())
        print(t)
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")
            print(t)

    return render(request,'lgp.html')
