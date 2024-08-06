# pandas dataframe 
import pandas as pd

data = {
    'cars' : ['tata','bmw','wols wagan','ford'],
    'sales' : [23,4,2,7]
}

# data frame
df = pd.DataFrame(data)
print(df)

# accessing index
print(df.loc[0],'\n\n')

# labbeled index
df = pd.DataFrame(data, index=['day1','day2','day3','day4'])
print(df.loc['day3'])