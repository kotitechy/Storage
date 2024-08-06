# prime numbers

def prime_numbers(n):
    pl = []
    npl = []
    for i in range(1, n):
        if n % i == 0:
            pl.append(i)
        else:
            npl.append(i)
    print(f'prime list : ', pl)
    print(f'composite list : ', npl)

prime_numbers(100)