import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(host = "localhost", port = 3306, user = "root", passwd ="", database = "collegelibrary")
    cursor = mydb.cursor()
    #cursor.execute("create table books(name varchar(258))")
    cursor.execute("create table Issuedbooks(student_name varchar(258), book_name varchar(258), issued_date varchar(258), retuern_date varchar(258))")

except Error as e:
    print("Error to connecting database ",e)