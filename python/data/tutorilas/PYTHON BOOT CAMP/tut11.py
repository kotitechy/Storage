# logical operators
# used in if statements
# 1. not
# 2. and 
# 3. or

mybool = True

if mybool:
    print("Yes It's True")
# 1.
if not mybool:
    print("It's False")

var1 = 2
# 2. 
if mybool and var1 == 2:
    print('if condition passed by and ')


var1 = 2
# 3. 
if not mybool or var1 == 2:
    print('if condition passed by or')