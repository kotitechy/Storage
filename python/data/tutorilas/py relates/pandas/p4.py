# pandas key/value objects as series
# label and data

import pandas as pd

data = {'day1':20,
        'day2':30,
        'day3':40,
        'day4':50 }

s1 = pd.Series(data)
print(s1)
# access labbled data
s1 = pd.Series(data, index=['day1','day3'])
print(s1)