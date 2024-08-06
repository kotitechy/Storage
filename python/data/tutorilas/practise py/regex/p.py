import os
import re

c = 0
pattren = r'foo|python3|abc123'
text = ['foo', 'python3', 'abc123']
for i in text:
    m = re.match(pattren, i)
    if m!= None:
        c+=1
    
    else:
        print('not ok')
print('Elements matched: ', c)