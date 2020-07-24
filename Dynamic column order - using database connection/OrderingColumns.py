import ConnectingToMySQL
import pandas as pd

#opening a connection to mysql
conn, message = ConnectingToMySQL.connectingMySQL()
print(message, " ", conn)

#opening a cursor to allow to execute the query
cur = conn.cursor()

#executing query in MariaDB to get the column names in the order that they have been created in the database
cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'TARGET_TABLE';")

record = cur.fetchall()
print(record)

#fetching the file to check what the order of columns in it are
path = "/Users/aakarsh.rajagopalan/Personal documents/Python projects/Dynamic column order - using database connection/Dynamic_column_order_file.csv"
df = pd.read_csv(path, header=0)
print(df.columns)



