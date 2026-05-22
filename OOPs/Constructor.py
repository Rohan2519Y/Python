# Constructor
# - bydefault each class contain a default constructor which is not visible
# - Constructor used to instantiate an object at the time of object declaration
# - Constructor invoke implicity when objects are declared
# 
# To create our own constructor we can use following function 
#   def __init__(self)
#   
# Destructors
# Destructor function invoke implicity before destroying any object
#   def__del__(self)
# 
# Statis Member Data
# - only one copy of static member is created for entire class and it share by all the objects
#   of same class no matter how many objects are created
# 
# Static Member Functions
# - also known as class methods or factory method
# - call with help class name
# - can access only static members
# 
# 
# 
# 
# 
########################################################################

# class Time:
#     def __init__(self,h=0,m=0,s=0):
#         self.__h=h
#         self.__m=m
#         self.__s=s

#     def putTime(self):
#         print(self.__h,self.__m,self.__s)

#     # def __add__(self, T):
#     def add(self, T):
#         R=Time()
#         R.__h=self.__h+T.__h
#         R.__m=self.__m+T.__m
#         R.__s=self.__s+T.__s

#         R.__m=R.__m+(R.__s//60)
#         R.__s=R.__s%60

#         R.__h=R.__h+(R.__m//60)
#         R.__m=R.__m%60

#         d=R.__h//24
#         print("DAYS :",d)
#         R.__h=R.__h%24

#         return R

# T1=Time(100,500,700)
# T2=Time(10,50,70)
# T1.putTime()
# T2.putTime()
# T3=T1.add(T2)
# T3.putTime()

# class Person:
#     def __init__(self, name):
#         self.__name=name
#         print("Person Created...",self.__name)

#     def ShowPerson(self):
#         print("Person :",self.__name)

#     def __del__(self):
#         print("Person Destroyed :",self.__name)

# P1=Person("Thomas")
# P2=Person("Vicky")
# P1.ShowPerson()
# P2.ShowPerson()
# # P3=P1
# # P3.ShowPerson()
# # del P1 
# P1=Person("Teena")
# P1.ShowPerson()
# input("End")



# class Bank:

#     __bankbalance=0
#     __count=0

#     def OpenAccount(self):
#         self.__acno=int(input("Enter Account Number : "))
#         self.__name=input("Enter Name : ")
#         self.__balance=int(input("Enter Balance : "))
#         Bank.__bankbalance+=self.__balance
#         Bank.__count+=1

#     def ShowAccount(self):
#         print(self.__acno, self.__name, self.__balance)

#     def Deposit(self):
#         amt=int(input("Enter Amount to Deposit : "))
#         self.__balance+=amt
#         Bank.__bankbalance+=amt

#     def Withdrawal(self):
#         amt=int(input("Enter Amount to Deposit : "))
#         self.__balance-=amt
#         Bank.__bankbalance-=amt

#     @classmethod
#     def ShowBankBalance(cls):
#         print(cls.__bankbalance,cls.__count)

# C1=Bank()
# C2=Bank()
# C3=Bank()
# C1.OpenAccount()
# C2.OpenAccount()
# C3.OpenAccount()
# C1.ShowAccount()
# C2.ShowAccount()
# C3.ShowAccount()
# Bank.ShowBankBalance()



# class Alien:
#     total = 0
#     def __init__(self, type):
#         if type == 'red' :
#             self.__point = 10
#             self.__type = 'red'
#         elif type == 'green' :
#             self.__point = 20
#             self.__type = 'green'

#     @classmethod
#     def ShowPoint(cls):  
#         print("Total Point :", cls.total)

#     def __del__(self):
#         Alien.total+=self.__point
#         print('Alien :', self.__type, "Destoyed")

# A1=Alien('red')
# A2=Alien('green')
# A3=Alien('red')
# Alien.ShowPoint()
# del A2
# Alien.ShowPoint()
# del A1
# Alien.ShowPoint()
# input("End")



# class TollRoad:

#     L = []
#     HV = 0
#     LV = 0
#     HVcount = 0
#     LVcount = 0
#     GVcount = 0

#     def __init__(self, vehicle_type):
#         yn = 'y'
#         while yn == 'y':
#             yn = input("Vehicle Coming (y/n): ")

#             if yn == 'y':
#                 vehicle_type = input("Enter Vehicle Type (HV/LV/GV): ")

#                 if vehicle_type == 'HV':
#                     self.__type = 'HV'
#                     self.__charge = 400
#                     TollRoad.HV += 400
#                     TollRoad.HVcount += 1

#                 elif vehicle_type == 'LV':
#                     self.__type = 'LV'
#                     self.__charge = 100
#                     TollRoad.LV += 100
#                     TollRoad.LVcount += 1

#                 elif vehicle_type == 'GV':
#                     self.__type = 'GV'
#                     self.__charge = 0
#                     TollRoad.GVcount += 1

#                 else:
#                     print("Invalid Type")
#                     continue

#                 TollRoad.L.append((self.__type, self.__charge))

#     def ShowVehicles(self):
#         print("Vehicles List:")
#         for v in TollRoad.L:
#             print("Type:", v[0], "Charge:", v[1])

#     def ShowTotal(self):
#         print("Total Amount:", TollRoad.HV + TollRoad.LV)
#         print("HV Count:", TollRoad.HVcount)
#         print("LV Count:", TollRoad.LVcount)
#         print("GV Count:", TollRoad.GVcount)


# T1 = TollRoad('HV')
# T1.ShowVehicles()
# T1.ShowTotal()


class Student:
    def GetStudent(self):
        self.__rollno=input("Enter Roll Number : ")
        self.__name=input("Enter Name : ")

    def GetMarks(self):
        self.__p=input("Enter Physics Marks : ")
        self.__c=input("Enter Chemistry Marks : ")
        self.__m=input("Enter Maths Marks : ")

    def DisplayStudent(self):
        print("Roll Number : ",self.__rollno)
        print("Name : ",self.__name)
        print("Physics Marks : ",self.__p)
        print("Chemistry Marks : ",self.__c)
        print("Maths Marks : ",self.__m)

    @staticmethod
    def ShowMarks(S):
        for s in S:    
            s.DisplayStudent()

    @staticmethod
    def Heading():
        print("-------------Data---------------")

    @staticmethod
    def Search(S,rollno):
        for s in S :
            if(s.__rollno==rollno):
                s.DisplayStudent()
                return True
        return False

L=[]
n=int(input("Enter Number : "))
for i in range(n):
    S1=Student()
    S1.GetStudent()
    S1.GetMarks()
    L.append(S1)

Student.ShowMarks(L)
rollno=input("Enter Roll Number : ")
found=Student.Search(L,rollno)
print(found)