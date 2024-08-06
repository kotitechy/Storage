class Library:
    books = [1,2]
    lb = []
    def ls_book(self):
        print('Now Books: ',self.books)
    def lend_book(self):
        self.ls_book()

    def return_book(self):
        pass
    def add_book(self):
        pass

class user(Library):
    usr=[]
    def register(self):
        print('Regsiter Section')
        n = input('Enter Your Name : ')
        id = int(input('Enter Your id: '))
        branch = input('Enter Your branch : ')
        yr = int(input('Enter your year : '))
        self.usr.append(n)
        self.usr.append(id)
    def authen(self):
        name = input('Enter Your Name : ')
        id_1 = int(input('Enter Your id: '))
        if  name == self.usr[0] and  id_1  == self.usr[1]:
            print('Login sucess')
        else:
            print('invalid credentials')
            exit()
            
    def lb(self):
        self.authen()
        self.n = {}
        src = int(input('Enter serial code of the book: '))
        self.books.pop(src)
        print('Take the book')
        self.n
        print('available books: ', self.books)
        self.lend_book()



l1 = Library()
# l1.ls_book()
s1 = user()
s1.register()
s1.lb()


