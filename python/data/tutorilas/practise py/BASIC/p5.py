# compund intrest 

def compund_intrest_calc(p ,t,r):
    a = p * pow((1 + r/100),t)
    ci = a - p 
    return ci

print("ci is : ",compund_intrest_calc(1000, 12, 1))
