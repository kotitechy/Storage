# sum of list elements

def sum_list(ls):
    s = 0 
    for i in ls:
        s = s + i
    print(f'sum of list elements : {s}')
ls=[1,2,34,4]
sum_list(ls)

# list methods
# length
ls  = [1,2,3,4,5,6,7,8,9]
print('Length of list is : ',len(ls))

# element exists in list 
# n = int(input('Enter element to b found: '))
def srch(n):
    if n in ls :
        print(f'Element Found at index-{ls.index(n)}')
    else:
        print('Element not found')

# srch(n)

# clear list
print('list elements: ',ls)
ls.clear()
print(ls)

ls  = [1,2,3,4,5,6,7,8,9]
# reverse list
print('Reverse list: ',ls[::-1])
ls  = [1,2,3,4,5,6,7,8,9]
# multiply list elements
def mul_list(ls):
    m = 1
    for i in ls:
        m = m * i
    print('Mul of list :', m)

mul_list(ls)

# min of list
def min_list(ls):
    print(f'min of list: {min(ls)}')
    ls.sort()
    print(f'min of list: {ls[0]}')

min_list(ls)

# max of list
def max_list(ls):
    print(f'max of ls is : ', max(ls))
    ls.sort()
    print(f'max of ls is : ', (ls[-1]))

max_list(ls)

# even/odd in list
def list_e_od(ls):
    el = []
    ol = []
    for i in range(len(ls)):
        if i % 2 == 0:
            el.append(i)
        else:
            ol.append(i)
    print('even is : ',el)
    print('Odd list : ', ol)

list_e_od(ls)

# even / odd in range
def e_o_r(ls, n):
    el = []
    ol = []
    for i in range(n):
        if i % 2 == 0:
            el.append(i)
        else:
            ol.append(i)
    print('Even are: ',el)
    print('odd are: ', ol)

e_o_r(ls, 10)

# +ve, -ve in list
ls = [-1,-2,-3,0,3,2,4,5]
def pos_neg(ls):
    nl = []
    pl = []
    for i in ls:
        if i < 0:
           nl.append(i) 
        else:
            pl.append(i)
    print('-ve are : ', nl)
    print('+ve are : ', pl)

pos_neg(ls)

# remove multiple elements inlist
ls  = [1,2,3,4,5,6,7,8,9]
n = int(input('How many elements to be removed: '))
print('new list is : ', ls[n:])

# copy list

ls  = [1,2,3,4,5,6,7,8,9]
new_ls = ls # copying list
print('Copied list: ',new_ls)
