import pandas as pd

#the following solution is when we as developers have control over the column order in the target env

#importing the file that has the dynamic column order
path = "/Users/aakarsh.rajagopalan/Personal documents/Python projects/Dynamic column order/Dynamic_column_order_file.csv"
df = pd.read_csv(path, header=0)

#printing the column names
print(df.columns)

#it is always advisable to order the columns alphabetically
df = df.sort_index(axis= 1)

#writing a new csv file with updated column order
output_filename = "Sorted_Dynamic_column_order_file.csv"

with open(output_filename, 'w') as f:
    print(df, file = f)

print("output to file complete")