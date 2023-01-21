import mysql.connector
from mysql.connector import Error
try:
    mydb = mysql.connector.connect(host = "Localhost", port = 3306, user = "root", passwd = "")
    cursor = mydb.cursor()
    cursor.execute("create database collegeLibrary") 

except Error as e:
    print("Error connecting to database",e)