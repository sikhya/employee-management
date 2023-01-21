import mysql.connector
from mysql.connector import Error
import re
try:
    conn=mysql.connector.connect(host= "localhost", port= 3306, user="root", passwd="", database="EmployeeData")
    cur=conn.cursor()
except Error as e:
    print("Error to connecting database.",e)



def AddEmployee():
    Id=int(input("Enter employee ID: "))
    if Check_Employee(Id)==True:
        print("Employee ID already exist please retry valid id...")
        input("Press any key to continue...")
        AddEmployee()

    Name=input("Enter employee name: ")
    if Check_Employee_Name(Name)==True:
        print("Employee Name already exist please retry...")
        input("Press any key to continue...")
        AddEmployee()

    EmailID=input("Enter email id: ")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, EmailID)):
        print("Valid Email")
    else:
        print("Invalid Email, Please enter valid email id...")
        input("\nPress any key to continue...")
        AddEmployee()

    PhoneNo=int(input("Enter phone number: "))
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    if (Pattern.match(str(PhoneNo))):
        print ("Valid Number")    
    else :
        print ("Invalid Number")
        AddEmployee()

    Address= input("Enter address: ")

    Post=input("Enter employee post: ")

    Salary=int(input("Enter employee salary: "))

    data=[Id,Name,EmailID,PhoneNo,Address,Post,Salary]
    sql="insert into Employee values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,data)
    conn.commit()
    print("succesfully insert data in table.")
    input("Press any key to continue...")
    menu()

def DisplayEmployee():
    cur.execute("select* from Employee")
    r = cur.fetchall()
    for i in r:
        print("Employee ID: ",i[0])
        print("Employee Name: ",i[1])
        print("Email id: ",i[2])
        print("Phone no.: ",i[3])
        print("Employee Address: ",i[4])
        print("Employee Post: ",i[5])
        print("Employee Salary: ",i[6])
        print("\n")
    input("Press any key to continue...")
    menu()


def UpdateEmployee():
    Id = int(input("Enter employee id: "))
    if Check_Employee(Id)==False:
        print("Employee ID not exist please retry valid id...")
        input("Press any key to continue...")
        UpdateEmployee()

    EmailID=input("Enter email id: ")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, EmailID)):
        print("Valid Email")
    else:
        print("Invalid Email, Please enter valid email id...")
        input("\nPress any key to continue...")
        UpdateEmployee()

    PhoneNo=int(input("Enter phone number: "))
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    if (Pattern.match(str(PhoneNo))):
        print ("Valid Number")    
    else :
        print ("Invalid Number")
        UpdateEmployee()

    Address= input("Enter address: ")

    sql="update Employee set Email_ID=%s, Phone_No=%s, Address=%s where Employee_ID=%s"
    data=[EmailID,PhoneNo,Address,Id]
    cur.execute(sql,data)
    conn.commit()
    print("Succefully update employee data.")
    input("Press any key to continue...")
    menu()


def PromoteEmployee():
    Id = int((input("Enter employee id: ")))
    if Check_Employee(Id)==False:
        print("Employee ID not exist please retry valid id...")
        input("Press any key to continue...")
        PromoteEmployee()
    Amount = int(input("Enter increase salary: "))
    sql = "select Salary from Employee where Employee_ID=%s"
    data = (Id,)
    cur.execute(sql,data)
    r = cur.fetchone()
    print(f"{r[0]}")
    t = r[0]+Amount
    sql = "update Employee set Salary= %s where Employee_ID= %s"
    data = (t,Id)
    cur.execute(sql,data)
    conn.commit()
    print("Employee promoted .")
    input("Press any key to continue...")
    menu()


def RemoveEmployee():
    Id = input("Enter employee id: ")
    if Check_Employee(Id)==False:
        print("Employee ID not exist please retry valid id...")
        input("Press any key to continue...")
        RemoveEmployee()
    cur.execute("delete from Employee where Employee_ID='"+Id+"'")
    conn.commit()
    print("Succefully remove empoyee data.")
    input(" Press any key to continue...")
    menu()


def SearchEmployee():
    Id = int(input("Enter employee id: "))
    sql="select * from Employee where Employee_ID=%s"
    data=(Id,)
    cur.execute(sql,data)
    r = cur.fetchall()
    for i in r:
        print("Employee id: ",i[0])
        print("Employee name: ",i[1])
        print("Email id: ",i[2])
        print("Phone no.: ",i[3])
        print("Employee Address: ",i[4])
        print("Employee Post: ",i[5])
        print("Employee Salary: ",i[6])
        print("\n")
    input("Press any key to continue...")
    menu()


def Check_Employee(Id):
    sql = "select * from Employee where Employee_ID=%s"
    data=(Id,)
    cur.execute(sql,data)
    re=cur.fetchall()
    r=cur.rowcount
    if r==1:
        return True
    else:
        return False


def Check_Employee_Name(name):
    sql = "select * from Employee where Employee_Name=%s"
    data=(name,)
    cur.execute(sql,data)
    re=cur.fetchall()
    r=cur.rowcount
    if r==1:
        return True
    else:
        return False


def menu():
    print("\n")
    print("{:>80}".format("########################################################"))
    print("{:>75}".format("---->>-->>Employee management system<<--<<----"))
    print("{:>80}\n\n".format("########################################################"))
    print('''
    1. Add Employee Record
    2. Display Employee Record
    3. Update Employee Record
    4. Promote Employee Record
    5. Remove Employee Record
    6. Search Employee Record
    7. Exit
    ''')
    choice=input("Enter your Choice [above option 1-7]: ")
    
    if choice=='1':
        AddEmployee()
    elif choice=='2':
        DisplayEmployee()
    elif choice=='3':
        UpdateEmployee()
    elif choice=='4':
        PromoteEmployee()
    elif choice=='5':
        RemoveEmployee()
    elif choice=='6':
        SearchEmployee()
    elif choice=='7':
        exit()
    else:
        print("Please enter valid option.")
        menu()

menu()