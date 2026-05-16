# PYMYSQL##########################################################
# this module contain various functions which use to establish communication between python and mysql
# install - pip install pymysql
# 
# import pymysql as sql
# 
# connect() use to establish connection with mysql
# cursor() it is use to create an object which is use to supply sql queries ot database
# 
# exception handling
# try : 
#    =====
#    =====
#    =====
#    =====
# except Exception as E:
#   print(E)
# 
# try : this block captures series of errors at run time and throw it to the expection block where user can control the error message
# 
# 
# 
# 

import pymysql as sql
# try:
#     DB = sql.connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         password='1234'
#     )

#     SMT = DB.cursor()
#     Q = 'CREATE DATABASE PythonPractice'
#     SMT.execute(Q)
#     print('Database Created')
#     DB.close()

# except Exception as e:
#     print("Error : ", e)


# try:
#     DB = sql.connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         password='1234',
#         database='PythonPractice'
#     )

#     SMT = DB.cursor()
#     Q = 'CREATE TABLE Employees(employeeid int primary key, empname varchar(50), city varchar(50))'
#     SMT.execute(Q)
#     print('Database Created')
#     DB.close()

# except Exception as e:
#     print("Error : ", e)



# try:
#     DB = sql.connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         password='1234',
#         database='pythonpractice'
#     )

#     SMT = DB.cursor()
#     EID = input("Enter Employee ID : ")
#     EName = input("Enter Employee Name : ")
#     ECity = input("Enter Employee City : ")

#     Q = f"Insert into employees values({EID}, '{EName}', '{ECity}')"
#     print(Q)
#     SMT.execute(Q)
#     print('Database Created')
#     DB.commit()
#     DB.close()

# except Exception as e:
#     print("Error : ", e)



# Show Data #####################################################################################################
# try:
#     DB = sql.connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         password='1234',
#         database='PythonPractice'
#     )

#     SMT = DB.cursor()
#     Q = 'Select * from Employees'
#     SMT.execute(Q)
#     Record = SMT.fetchall()
#     print(Record)
#     DB.close()

# except Exception as e:
#     print("Error : ", e)


# Dict #####################################################################################################
# try:
#     DB = sql.connect(
#         host = 'localhost',
#         port = 3306,
#         user = 'root',
#         password = '1234',
#         database = 'PythonPractice',
#         cursorclass = sql.cursors.DictCursor
#     )

#     SMT = DB.cursor()
#     Q = 'Select * from Employees'
#     SMT.execute(Q)
#     Record = SMT.fetchall()
#     print(Record[0]['employeeid'])
#     DB.close()

# except Exception as e:
#     print("Error : ", e)



# Search #####################################################################################################
# try:
#     DB = sql.connect(
#         host = 'localhost',
#         port = 3306,
#         user = 'root',
#         password = '1234',
#         database = 'PythonPractice',
#         cursorclass = sql.cursors.DictCursor
#     )

#     SMT = DB.cursor()
#     inpt=input("Enter ID : ")
#     Q = f'Select * from Employees where employeeid={inpt}'
#     SMT.execute(Q)
#     Record = SMT.fetchall()
#     if Record : 
#         print(Record)
#     else : 
#         print("Record Not Found")
#     DB.close()

# except Exception as e:
#     print("Error : ", e)




# Range #####################################################################################################
# try:
#     DB = sql.connect(
#         host = 'localhost',
#         port = 3306,
#         user = 'root',
#         password = '1234',
#         database = 'PythonPractice',
#         cursorclass = sql.cursors.DictCursor
#     )

#     SMT = DB.cursor()
#     min=input("Enter Min : ")
#     max=input("Enter Max : ")
#     Q = f'Select * from Employees where city between {min} and {max}'
#     SMT.execute(Q)
#     Record = SMT.fetchall()
#     if Record : 
#         print(Record)
#     else : 
#         print("Record Not Found")
#     DB.close()

# except Exception as e:
#     print("Error : ", e)




# Edit #####################################################################################################\
# try:
#     DB = sql.connect(
#         host = 'localhost',
#         port = 3306,
#         user = 'root',
#         password = '1234',
#         database = 'PythonPractice',
#         cursorclass = sql.cursors.DictCursor
#     )

#     SMT = DB.cursor()
#     id = input("Enter Employee ID : ")
#     Q = f'Select * from Employees where employeeid = {id}'
#     SMT.execute(Q)
#     Record = SMT.fetchone()
#     if Record : 
#         print("Employee ID : ",Record['employeeid'])
#         print("1- Employee Name : ",Record['empname'])
#         print("2- Employee City : ",Record['city'])
#         print("3- Exit : ")
#         ch = int(input("Enter Your Choice : "))
#         pat = ''
#         if ch == 1:
#             en = input("Enter New Employee Name : ")
#             pat = f"empname = '{en}'"
#         elif ch == 2 :
#             ec = input("Enter New City : ")
#             pat = f"city = '{ec}'"
#         elif ch == 3 : 
#             print("Exit")
#         else : 
#             print("Wrong Option")

#         if pat != '' :
#             Q = f"Update employees set {pat} where employeeid = {id}"
#             SMT.execute(Q)
#             DB.commit()
#             print("Employee Update Successfully")
#     else : 
#         print("Record Not Found")
#     DB.close()

# except Exception as e:
#     print("Error : ", e)




# Delete #####################################################################################################
# try:
#     DB = sql.connect(
#         host = 'localhost',
#         port = 3306,
#         user = 'root',
#         password = '1234',
#         database = 'PythonPractice',
#         cursorclass = sql.cursors.DictCursor
#     )

#     SMT = DB.cursor()
#     id = input("Enter Employee ID : ")
#     Q = f'Select * from Employees where employeeid = {id}'
#     SMT.execute(Q)
#     Record = SMT.fetchone()
#     if Record : 
#         print("Employee ID : ",Record['employeeid'])
#         ch = input("Do you want to delete Y/N: ")
#         if ch.lower() == 'y' :
#             Q = f"Delete from employees where employeeid = {id}"
#             SMT.execute(Q)
#             DB.commit()
#             print("Employee Deleted Successfully")
#         else :
#             print("Cancel")
#     else : 
#         print("Record Not Found")
#     DB.close()

# except Exception as e:
#     print("Error : ", e)