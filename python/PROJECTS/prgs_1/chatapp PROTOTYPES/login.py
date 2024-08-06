from userfuncs  import con

class login():
    def log(self):
        

        try:
            n = input('Enter your name: ')
            mobile = int(input('Enter your mobile no : '))
            l = con()
            c = l[0]
            db = l[1]

            q = 'select name, mobile from kinter.users where name = %s or mobile = %s'
            d = [n,mobile]
            c.execute(q, d)
            r = c.fetchone()

            if n == r[0] and mobile == r[1]:
                print('login sucess \nwelcome',n)
            else:
                print('invalid credentials')



        except Exception as e:
            print(e)

l1 = login()
l1.log()