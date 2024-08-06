import os
from datetime import datetime as dt

print(dir(os))

print(len(dir(os)))

# get current directry
print(os.getcwd())

#change directry
os.chdir('c:/Users/SHIVA/pictures')

print(os.getcwd())

# list items
print(os.listdir())

# create a new folder
# os.makedir('os-demo1') # makes single directry
# os.makedirs('os-demo1/os-demo')  # makes sub directries

# os.makedirs('ks')

# remove directries
# print(os.rmdir('ks')) # rempoves single directry
# print(os.removedirs('os-demo1/os-demo')) # removes with sub and main folders

# rename a folder
# os.rename('k.jpg','karthik.jpg')

# info about files
r = os.stat('shiva.txt').st_size
r = os.stat('shiva.txt')
r = os.stat('shiva.txt').st_mtime # date time modified
print("Data is : \n ", r)

print(dt.fromtimestamp(r))

# to see entire directry tree
for dirpath, dirnames, filenames in os.walk('c:/Users/SHIVA/Desktop'):
    print('current path : ', dirpath)
    print('directries : ', dirnames)
    print('Files : ', filenames)

# access envrinomment variables
