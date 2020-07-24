import mysql.connector
from mysql.connector import Error

def connectingMySQL():
    #using a try and except block to catch exceptions during connection

    try:
        conn = mysql.connector.connect(host="localhost"
                                       , database="Aakarsh_db"
                                       , user = "root"
                                       , password = "")

        if conn.is_connected():
            db_info = conn.get_server_info()
            print("connection successful: ", db_info)
        return conn, "Connection successful"
    except Error as e:
        print("error while connecting to mysql: ",e )
        return conn, "Connection failed"
