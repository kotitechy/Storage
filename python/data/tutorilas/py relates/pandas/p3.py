# read csv file

import pandas as pd

# read csv
df = pd.read_csv('data.csv')
print(df)

# display all rows
print(df.to_string())

# set max values
pd.options.display.max_rows = 500 
df = pd.read_csv('data.csv')
print(df)  # prints full data set


