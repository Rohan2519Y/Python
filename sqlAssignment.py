# Database my_industry
# table products
#   ProductId, ProductName, QuantityPerUnit, UnitPrice, UnitInStock, UnitsOnOrder, ReorderLevel, Discountinued, MFG
# 
# 

import pymysql as sql


# Create Database #########################################################################################################
# try:
#     DB = sql.connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         password='1234'
#     )

#     SMT = DB.cursor()
#     Q = 'Create database my_industry'
#     SMT.execute(Q)
#     print("Database Created")
# except Exception as E:
#     print('Error : ',E)


# Create Table #########################################################################################################
# try:
#     DB = sql.connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         password='1234',
#         database='my_industry'
#     )

#     SMT = DB.cursor()
#     Q = '''create table products(
#                     ProductId int(11) primary key, 
#                     ProductName varchar(45), 
#                     QuantityPerUnit varchar(45), 
#                     UnitPrice varchar(45), 
#                     UnitInStock varchar(45), 
#                     UnitsOnOrder varchar(45), 
#                     ReorderLevel varchar(45), 
#                     Discountinued varchar(45),
#                     MFG varchar(45))'''
#     SMT.execute(Q)
#     print("Table Created")
# except Exception as E:
#     print('Error : ',E)



# Insert Data #########################################################################################################
# try:
#     DB = sql.connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         password='1234',
#         database='my_industry'
#     )

#     SMT = DB.cursor()
#     Q = '''insert into products values
#             (1, 'Pepsi', '4', '100', '10', '50', '30', '0', '14-11-2025'),
#             (2, 'Cola', '7', '120', '5', '60', '50', '0', '24-01-2025'),
#             (3, 'Fanta', '1', '110', '9', '70', '30', '1', '18-16-2025'),
#             (4, 'Frooti', '9', '130', '4', '80', '40', '0', '09-12-2025'),
#             (5, 'Mazza', '6', '90', '2', '30', '20', '0', '12-03-2025')'''
#     SMT.execute(Q)
#     DB.commit()
#     DB.close()
#     print("Data Inserted")
# except Exception as E:
#     print('Error : ',E)



# Retrieve Data #########################################################################################################
# try:
#     DB = sql.connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         password='1234',
#         database='my_industry',
#         cursorclass=sql.cursors.DictCursor
#     )

#     SMT = DB.cursor()
#     Q = '''Select * from products'''
#     SMT.execute(Q)
#     Records = SMT.fetchall()
#     for Record in Records : 
#         print(Record)
# except Exception as E:
#     print('Error : ',E)




# Edit #####################################################################################################\
# try:
#     DB = sql.connect(
#         host = 'localhost',
#         port = 3306,
#         user = 'root',
#         password = '1234',
#         database = 'my_industry',
#         cursorclass = sql.cursors.DictCursor
#     )

#     SMT = DB.cursor()
#     id = input("Enter Product ID : ")
#     Q = f'Select * from products where ProductId = {id}'
#     SMT.execute(Q)
#     Record = SMT.fetchone()
#     if Record : 
#         print("Product ID : ",Record['ProductId'])
#         print("1- Product Name : ",Record['ProductName'])
#         print("2- Quantity Per Unit : ",Record['QuantityPerUnit'])
#         print("3- Unit Price : ",Record['UnitPrice'])
#         print("4- Unit In Stock : ",Record['UnitInStock'])
#         print("5- Unit On Order : ",Record['UnitsOnOrder'])
#         print("6- Reorder Level : ",Record['ReorderLevel'])
#         print("7- Discountinued : ",Record['Discountinued'])
#         print("8- MFG : ",Record['MFG'])
#         print("9- Exit : ")
#         ch = int(input("Enter Your Choice : "))
#         pat = ''
#         if ch == 1:
#             en = input("Enter New Product Name : ")
#             pat = f"ProductName = '{en}'"
#         elif ch == 2 :
#             en = input("Enter Quantity Per Unit : ")
#             pat = f"QuantityPerUnit = '{en}'"
#         elif ch == 3 :
#             en = input("Enter Unit Price : ")
#             pat = f"UnitPrice = '{en}'"
#         elif ch == 4 :
#             en = input("Enter Unit In Stock : ")
#             pat = f"UnitInStock = '{en}'"
#         elif ch == 5 :
#             en = input("Enter Unit On Order : ")
#             pat = f"UnitsOnOrder = '{en}'"
#         elif ch == 6 :
#             en = input("Enter Reorder Level : ")
#             pat = f"ReorderLevel = '{en}'"
#         elif ch == 7 :
#             en = input("Enter Discountinued : ")
#             pat = f"Discountinued = '{en}'"
#         elif ch == 8 :
#             en = input("Enter MFG : ")
#             pat = f"MFG = '{en}'"
#         elif ch == 9 : 
#             print("Exit")
#         else : 
#             print("Wrong Option")

#         if pat != '' :
#             Q = f"Update products set {pat} where ProductId = {id}"
#             SMT.execute(Q)
#             DB.commit()
#             print("Products Update Successfully")
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
#         database = 'my_industry',
#         cursorclass = sql.cursors.DictCursor
#     )

#     SMT = DB.cursor()
#     id = input("Enter Product ID : ")
#     Q = f'Select * from Products where ProductId = {id}'
#     SMT.execute(Q)
#     Record = SMT.fetchone()
#     if Record : 
#         print("Product ID : ",Record['ProductId'])
#         ch = input("Do you want to delete Y/N: ")
#         if ch.lower() == 'y' :
#             Q = f"Delete from products where ProductId = {id}"
#             SMT.execute(Q)
#             DB.commit()
#             print("Product Deleted Successfully")
#         else :
#             print("Cancel")
#     else : 
#         print("Record Not Found")
#     DB.close()

# except Exception as e:
#     print("Error : ", e)