import ConnectingToMySQL
import pandas as pd

#opening a connection to mysql
conn, message = ConnectingToMySQL.connectingMySQL()
print(message, " ", conn)

#opening a cursor to allow to execute the query
cur = conn.cursor()
cur.execute("describe target_table;")
record = cur.fetchall()
print(record)

