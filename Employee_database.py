import mysql.connector
from mysql.connector import Error

try:
    db=mysql.connector.connect(host="localhost", port= 3306, user="root", passwd="")
    cursor=db.cursor()
    cursor.execute("create database EmployeeData")
except Error as e:
    print("Error conecting database",e)
