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