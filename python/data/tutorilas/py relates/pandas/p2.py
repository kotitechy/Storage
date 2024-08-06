# pandas series
import pandas as pd

data = [1,2,3,4,5,6]

# series
s = pd.Series(data)
print(s)

# accessing an index
print(s[3])

# adding labeled index 
s = pd.Series(data, index=['day1','day2','day3','day4','day5','day6'])
print(s)

# acessing labelled index
print(s['day1'])