import re

pattern = r'b'
text = 'a'
x = re.match(pattern, text) 
if x!=None:
    print('ok', x)
else:
    print('not ok')