# Inheritance
# types of inheritance
# - single inheritance
# - mulltilevel
# - hirarchical
# - multiple
# - hybrid
# 
# Single Inheritance
#   
#   Base(parent)
#       |
#       |
#   Derive Class (Child Class)
# 
# Visiblity Mode of Inheritance
# - private member(__) of base class are not inheritable one can access 
# these member only with the help of public members declared in base class
# 
# - public members are inheritable and can access by derive class directly
# - these members even access by objects outside the class defination
# - protected (_) can access by derive class directly but cannot use outside the class defination
# 
# 
# Hirarchical Inheritance
# 
# 
# 
# Multiple Inheritance
# 
# 
# Constructor in Inheritance
# class A:
# 
# 
# class B(A):
# 
# 
# t=B()
# - By default child class constructor implicity invokes the base class constructor
# 
# 



# SingleLevelClass #####################################################
# class Student:
#     def getStudent(self):
#         self.__rollno=input("Enter Roll Number : ")
#         self.__name=input("Enter Name : ")

#     def showStudent(self):
#         print(self.__rollno, self.__name)

# class Bsc(Student):
#     def getSubject(self):
#         self.getStudent()
#         self.__p=int(input("Enter Physics Marks : "))
#         self.__c=int(input("Enter Chemistry Marks : "))
#         self.__m=int(input("Enter Maths Marks : "))

#     def showSubjects(self):
#         self.showStudent()
#         print(self.__p, self.__c, self.__m)

# S=Bsc()
# S.getSubject()
# S.showSubjects()



# MultiLevelClass #####################################################
# class Student:
#     def getStudent(self):
#         self.__rollno=input("Enter Roll Number : ")
#         self.__name=input("Enter Name : ")

#     def showStudent(self):
#         print(self.__rollno, self.__name)

# class Bsc(Student):
#     def getSubject(self):
#         self.getStudent()
#         self._p=int(input("Enter Physics Marks : "))
#         self._c=int(input("Enter Chemistry Marks : "))
#         self._m=int(input("Enter Maths Marks : "))

#     def showSubjects(self):
#         self.showStudent()
#         print(self._p, self._c, self._m)

#     def getTotal(self):
#         t=self._p + self._c + self._m
#         return t

# class Result(Bsc):
#     def getResult(self):
#         self.getSubject()
#         self.__total=self.getTotal()

#     def showResult(self):
#         self.showSubjects()
#         print(self.__total)

# S=Result()
# S.getResult()
# S.showResult()


# Hirarchical Inheritance###################################################
# class Student:
#     def getStudent(self):
#         self.__rollno=input("Enter Roll Number : ")
#         self.__name=input("Enter Name : ")

#     def showStudent(self):
#         print(self.__rollno, self.__name)

# class Bsc(Student):
#     def getSubject(self):
#         self.getStudent()
#         self.__p=int(input("Enter Physics Marks : "))
#         self.__c=int(input("Enter Chemistry Marks : "))
#         self.__m=int(input("Enter Maths Marks : "))

#     def showSubjects(self):
#         self.showStudent()
#         print(self.__p, self.__c, self.__m)

# class Ba(Student):
#     def getSubject(self):
#         self.getStudent()
#         self.__e=int(input("Enter Economics Marks : "))
#         self.__g=int(input("Enter Geography Marks : "))
#         self.__h=int(input("Enter History Marks : "))

#     def showSubjects(self):
#         self.showStudent()
#         print(self.__e, self.__g, self.__h)

# S1=Bsc()
# S2=Ba()
# S1.getSubject()
# S1.showSubjects()
# S2.getSubject()
# S2.showSubjects()


# Multiple Inheritance###################################################
# class ProductionOne:
#     def getProductionOne(self):
#         self._one=int(input("Total Production One: "))

#     def showProductionOne(self):
#         print("Production One :", self._one)

# class ProductionTwo:
#     def getProductionTwo(self):
#         self._two=int(input("Total Production Two: "))

#     def showProductionTwo(self):
#         print("Production Two :", self._two)

# class TotalProduction(ProductionOne,ProductionTwo):
#     def getTotal(self):
#         self.getProductionOne()
#         self.getProductionTwo()
#         self.__total=self._one + self._two

#     def putTotal(self):
#         self.showProductionOne()
#         self.showProductionTwo()
#         print("Total Production : ", self.__total)

# C=TotalProduction()
# C.getTotal()
# C.putTotal()    


# Hybrid Inheritance###################################################
class Company:
    def getCompany(self):
        self.__cn=input("Enter Company Nmae : ")

    def showCompany(self):
        print(self.__cn)
    

class ProductionOne(Company):
    def getProductionOne(self):
        self._one=int(input("Total Production One: "))

    def showProductionOne(self):
        print("Production One :", self._one)

class ProductionTwo(Company):
    def getProductionTwo(self):
        self._two=int(input("Total Production Two: "))

    def showProductionTwo(self):
        print("Production Two :", self._two)

class TotalProduction(ProductionOne,ProductionTwo):
    def getTotal(self):
        self.getCompany()
        self.getProductionOne()
        self.getProductionTwo()
        self.__total=self._one + self._two

    def putTotal(self):
        self.showCompany()
        self.showProductionOne()
        self.showProductionTwo()
        print("Total Production : ", self.__total)

C=TotalProduction()
C.getTotal()
C.putTotal() 