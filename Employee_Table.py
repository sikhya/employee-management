import mysql.connector
from mysql.connector import Error

try:
    db=mysql.connector.connect(host= "localhost", port= 3306, user="root", passwd="", database="EmployeeData")
    cursor=db.cursor()
    cursor.execute("create table Employee(Employee_ID int(20) primary key,Employee_Name varchar(1000),Email_ID text(1000),Phone_No bigint(100),Address text(1000),Post text(1000),Salary bigint(100))")
except Error as e:
    print("Error to conecting to database",e)
