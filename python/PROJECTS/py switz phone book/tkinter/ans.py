maths = [4,3,2,1,3,2,2,3,2,3,1,4,3,1,1,3,3,2,3,2,4,3,1,4,2,1,3,4,3,3,2,1,4,4,3,1,3,4,1,3,2,4,4,2,3,4,2,3,4,1]
physics = [3,2,2,3,4,3,2,3,1,3,2,1,1,4,3,4,3,4,1,1,4,2,1,2]
chem =    [3,4,3,2,3,1,4,4,2,3,3,3,2,2,4,1,1,1,3,3,2,2,1,4,1]
core =    [1,4,4,4,4,3,2,4,2,3,2,1,2,3,4,2,4,3,1,3,2,3,4,1,2,3,4,1,2,1,3,1,1,2,1,3,1,4,2,4,3,3,2,3,3,3,2,3,3,4,2,1,4,1,4,2,3,1,3,4,3,3,1,4,3,1,3,2,1,3,4,3,4,3,4,2,2,4,3,1,2,3,1,1,4,4,2,3,1,4,1,2,1,4,3,2,2,1,4,4,4]

m22 = [1,4,2,1,4,3,4,1,2,1,3,2,2,3,2,4,4,3,1,4,4,1,2,3,1,4,3,1,2,3,3,2,3,2,3,3,3,2,1,3,1,3,3,2,4,3,4,1,4,4,2,1]
p22 = [3,3,1,3,3,2,1,4,1,1,3,4,2,3,2,1,4,2,1,4,2,1,3,4,2]
ch22 = [1,4,2,1,2,2,2,4,3,4,4,3,2,4,4,4,2,1,2,1,2,3,4,1,1]
c22 = [2,1,1,3,2,4,3,2,1,4,3,3,1,3,3,4,2,2,1,4,2,4,2,4,3,4,3,1,2,3,4,3,1,1,2,4,2,1,2,1,1,3,4,4,3,2,1,1,3,3,3,3,2,2,3,3,4,4,1,3,2,2,4,4,2,4,2,2,4,2,1,2,4,2,2,2,1,4,3,4,2,2,2,1,2,1,1,4,2,2,3,4,2,3,3,3,3,1,3,]


m21= [2,2,2,3,2,2,3,3,2,2,3,4,1,3,3,3,4,4,3,2,1,3,2,4,1,2,2,3,3,3,3,4,2,2,1,3,4,2,1,2,1,2,3,3,1,2,4,3,4,2]
p21 = [3,1,1,1,4,3,4,3,2,4,3,3,4,1,1,4,1,4,3,1,3,4,4,1,2]
ch21  = [4,2,1,2,3,3,3,1,1,2,3,4,3,1,2,4,3,1,1,4,1,4,1,1,4] 
c21 = [3,2,4,1,3,1,2,4,4,1,2,1,1,1,3,4,3,4,3,2,2,2,3,3,3,1,2,3,1,3,2,4,2,2,3,2,1,1,3,4,1,3,3,1,1,4,4,3,4,1,4,1,2,2,4,3,4,3,4,1,1,2,3,2,2,1,3,4,3,3,3,4,3,4,3,2,1,3,2,3,3,3,4,3,4,3,3,4,3,4,4,3,3,2,1,4,3]




ans = [maths, physics,chem,core]
print()
anns = []
for i in ans:
    for j in i:
        anns.append(j)

print('Total', len(anns))


def func(ls, su):
    from collections import Counter
    counts = Counter(ls)

    anns = []
    print(f'subject {su}')
    for i, c in counts.items():
        print(f'{i} is repeated {c}, times')


func(m22, 'maths')
func(p22, 'physcis ')
func(ch22, 'chemistry')
func(c22, 'core')