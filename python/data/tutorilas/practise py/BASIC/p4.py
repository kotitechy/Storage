# simple intreset

p = int(input("Enter a amount : "))
t = int(input("Enter Time-period: "))
r = int(input("Enter rate of intreset: "))

def simple_intrest_calc(p, t, r):
    return (p * t* r) / 100

simple_intrest_calc(p, t, r)