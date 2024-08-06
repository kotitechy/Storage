# factorial of number

def fact(n):
    if n <=0 :
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))

# m-2
def facto(n):
    f = 0 
    if n <= 0:
        f = 1
    else:
        o = 1
        for i in range(1, n):
            o = o * i
        f = o
    print(f'fact of {n}: {f}')

facto(5)
