'''
Authour: shiva
program : gym management using files
language: python
'''

class hm:
    def __init__(self) -> None:
        try:
            f = open('users.txt', 'x')
            f.close()
        except Exception as e:
            # print(e)
            pass
        
    def tsmp(self):
        import datetime as dt
        d = dt.datetime.now()
        return d
    def usr(self, n, a, w):
        f = open('user_folder.txt', "a")
        p = f.tell()
        print(p)
        p += 1
        f.write(f"\n Name : {n}, age : {a}, weight : {w}")
        f.close()
        print(f'User with {n} created')
    def register(self):
        print('Regsiter Section')
        n = input('Enter Your Name : ')
        age = int(input('Enter Your Age: '))
        wgt = int(input('Enter Your Weight : '))

        f = open('users.txt', "a")

        p = f.tell()
        print(p)
        p += 1
        f.write(f"{n} \n")
        f.close()
        self.usr(n, age, wgt)
        print(f'User with {n} created')

        f = open(f'{n}.txt', 'x')
        f.close()

    def ret(self):
        u = input('Enter Your name : ')
        f = open('users.txt','r')
        for line in f:
            if u in line:
                print('Logged in')
            else:
                print('no such user exists \n u can register first')
        print('1. retrive Data \n2. Lock Data \nchoose an operation')
        op = int(input())
        c = 0
        if op == 1:
                print('Retrieving data')
                f = open(f'{u}.txt','r')
                for l in f.readlines():
                    print(l)
                    c+=1
                print("Total: ", c-1, "Days")
                f.close()
        elif op ==2:
            n = int(input('Enter the no of Excercises: '))
            
            ex=[]
            p = f.tell()
            print(p)
            ts = self.tsmp()
            for i in range(n):
                exrs = input(f'Enter {i+1}th Excercise: ')
                ex.append(exrs)
                print(ex)
            
            f = open(f'{u}.txt', "a")
            p = f.tell()
            p+10
            f.write(f'\ntime: {ts}, excercises: {n}, {ex}')
            f.close()


h1 = hm()
r = True
while r:
    a = int(input('1. Register \n2. login \n3. Exit \nChoose an Option: '))
    if a == 1:
        h1.register()
    elif a == 2:
        h1.ret()
    elif a == 3:
        break
    else:
        print('choose an valid option')
