import pandas as pd

#importing the file that has the dynamic column order
path = "/Users/aakarsh.rajagopalan/Personal documents/Python projects/Dynamic column order/Dynamic_column_order_file.csv"
df = pd.read_csv(path, header=0)

#printing the column names
print(df.columns)

#it is always advisable to order the columns alphabetically
df = df.sort_index(axis= 1)
print(df)