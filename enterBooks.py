import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(host = "localhost", port = 3306, user = "root", passwd ="", database = "collegelibrary")
    cursor = mydb.cursor()
    entryBook = True
    while entryBook:
        nm = input("Enter book name or press q for complete book entry: ")
        if nm != "q":
            query = "insert into books(name) values('"+nm+"')"
            cursor.execute(query)
            mydb.commit()
        elif nm == "q":
            entryBook = False

except Error as e:
    print("Error to connecting database ",e)