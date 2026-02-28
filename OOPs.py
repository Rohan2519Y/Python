# class <class name>:
#   ===member functions
#   ===member data
# 
# class contains three types of member
# - private
#   members which declare private are totaly hidden and can not access by any external function,
#   only the member function which declare in public section of class can access these members.
#   __varname 
# 
# - public
#   members which declare public within the class can access by any external functions
#   varname
# 
# - protected
#   _varname
################################################################################################################ 

# class Student:
#     def GetStudent(self):
#         self.__rollno=input("Enter Roll Number : ")
#         self.__name=input("Enter Name : ")

#     def GetMarks(self):
#         self.__p=input("Enter Physics Marks : ")
#         self.__c=input("Enter Chemistry Marks : ")
#         self.__m=input("Enter Maths Marks : ")

#     def ShowMarks(self):
#         print("Roll Number : ",self.__rollno)
#         print("Name : ",self.__name)
#         print("Physics Marks : ",self.__p)
#         print("Chemistry Marks : ",self.__c)
#         print("Maths Marks : ",self.__m)

#     @staticmethod
#     def Heading():
#         print("-------------Data---------------")

# L=[]
# n=int(input("Enter Number : "))
# for i in range(n):
#     S1=Student()
#     S1.GetStudent()
#     S1.GetMarks()
#     L.append(S1)
# Student.Heading()
# for STD in L:
#     STD.ShowMarks()

# class Employee:
#     def GetEmployee(self):
#         self.__id=input("Enter ID : ")
#         self.__name=input("Enter Name : ")
#         self.__salary=int(input("Enter Salary : "))

#     def GetSalary(self):
#         self.__da=self.__salary*(20/100)
#         self.__hra=self.__salary*(10/100)
#         self.__pf=self.__salary*(5/100)
#         self.__ns=self.__salary+self.__da+self.__hra-self.__pf

#     def ShowEmployee(self):
#         print("============Employee Data============")
#         print("Employee ID : ",self.__id)
#         print("Name : ",self.__name)
#         print("Salary : ",self.__salary)
#         print("DA : ",self.__da)
#         print("HRA : ",self.__hra)
#         print("PF : ",self.__pf)
#         print("Net Salary : ",self.__ns)

#     @staticmethod
#     def Heading():
#         print("--------------------Heading-------------------")

# S1=Employee()
# S1.Heading()
# S1.GetEmployee()
# S1.GetSalary()
# S1.ShowEmployee()

########################################################################################################################

# import os
# class Product:
#     def GetProduct(self):
#         self.__id=int(input("Enter Product Id : "))
#         self.__name=input("Enter Product Name : ")
#         self.__rate=int(input("Enter Product Rate : "))
#         self.__stock=int(input("Enter Product Stock : "))

#     def ShowProduct(self):
#         print(f"{self.__id}\t{self.__name}\t{self.__rate}\t{self.__stock}\t")

#     def Search(self,id):
#         if self.__id==id:
#             return True
#         else:
#             return False
        
#     def Sale(self):
#         qty=int(input("Enter Quantity : "))
#         if qty <= self.__stock:
#             amt=self.__stock*qty
#             print("Amount : ",amt)
#             self.__stock-=qty
#         else:
#             print("Insuffiecient Stock...")

#     def Purchase(self):
#         qty=int(input("Enter Quantity : "))
#         self.__stock+=qty

    
# L=[]
# n=int(input("Enter Number : "))
# for i in range(n):
#     P=Product()
#     P.GetProduct()
#     L.append(P)
# os.system('cls')

# while(True):
#     os.system('cls')
#     print("Main Menu")
#     print("1: Display All\n2: Search By Id\n3: Sale\n4: Purchase\n5: Exit\n")
#     ch=int(input("Enter Your Choice : "))
#     if ch==1 :
#         for p in L:
#             p.ShowProduct()
#         input("Press Enter To Continue...")

#     elif ch==2 :
#         id=int(input("Enter ID : "))
#         for p in L:
#             found=p.Search(id)
#             if found : 
#                 p.ShowProduct()
#                 break
#         if not found :
#             print(f"Product Not Found : {id}")
#         input("Press Enter To Continue...")

#     elif ch==3 :
#         id=int(input("Enter Product ID : "))
#         for p in L:
#             found=p.Search(id)
#             if found : 
#                 p.ShowProduct()
#                 p.Sale()
#                 break
#         if not found :
#             print(f"Product Not Found : {id}")
#         input("Press Enter To Continue...")

#     elif ch==4 :
#         id=int(input("Enter Product ID : "))
#         for p in L:
#             found=p.Search(id)
#             if found : 
#                 p.ShowProduct()
#                 p.Purchase()
#                 break
#         if not found :
#             print(f"Product Not Found : {id}")
#         input("Press Enter To Continue...")

#     elif ch==5:
#         print("Exiting...")
#         break

#     else:
#         print("Wrong Option")
#         input("Press Enter To Continue")

import os
class Product:
    def GetProduct(self):
        self.__id=int(input("Enter Product Id : "))
        self.__name=input("Enter Product Name : ")
        self.__rate=int(input("Enter Product Rate : "))
        self.__stock=int(input("Enter Product Stock : "))
        return self.__id

    def ShowProduct(self):
        print(f"{self.__id}\t{self.__name}\t{self.__rate}\t{self.__stock}\t")

    def Search(self,id):
        if self.__id==id:
            return True
        else:
            return False
        
    def Sale(self):
        qty=int(input("Enter Quantity : "))
        if qty <= self.__stock:
            amt=self.__stock*qty
            print("Amount : ",amt)
            self.__stock-=qty
        else:
            print("Insuffiecient Stock...")

    def Purchase(self):
        qty=int(input("Enter Quantity : "))
        self.__stock+=qty

    
L=[]
n=int(input("Enter Number : "))
for i in range(n):
    P=Product()
    key=P.GetProduct()
    L.setdefault(key,P)
    
os.system('cls')

while(True):
    os.system('cls')
    print("Main Menu")
    print("1: Display All\n2: Search By Id\n3: Sale\n4: Purchase\n5: Exit\n")
    ch=int(input("Enter Your Choice : "))
    if ch==1 :
        for p in L.values():
            p.ShowProduct()
        input("Press Enter To Continue...")

    elif ch==2 :
        id=int(input("Enter ID : "))
        P=L.get(id,"Product Not Found")
        if(isinstance(P,Product)):
            P.ShowProduct()
        else:
            print(P)
        input("Press Enter To Continue...")

    elif ch==3 :
        id=int(input("Enter ID : "))
        P=L.get(id,"Product Not Found")
        if(isinstance(P,Product)):
            P.ShowProduct()
            P.Sale()
        else:
            print(P)
        input("Press Enter To Continue...")

    elif ch==4 :
        id=int(input("Enter ID : "))
        P=L.get(id,"Product Not Found")
        if(isinstance(P,Product)):
            P.ShowProduct()
            P.Purchase()
        else:
            print(P)
        input("Press Enter To Continue...")

    elif ch==5:
        print("Exiting...")
        break

    else:
        print("Wrong Option")
        input("Press Enter To Continue...")