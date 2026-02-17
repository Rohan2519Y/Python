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
#         print("============Student Data============")
#         print("Roll Number : ",self.__rollno)
#         print("Name : ",self.__name)
#         print("Physics Marks : ",self.__p)
#         print("Chemistry Marks : ",self.__c)
#         print("Maths Marks : ",self.__m)

# S1=Student()
# S1.GetStudent()
# S1.GetMarks()
# S1.ShowMarks()

class Employee:
    def GetEmployee(self):
        self.__id=input("Enter ID : ")
        self.__name=input("Enter Name : ")
        self.__salary=int(input("Enter Salary : "))

    def GetSalary(self):
        self.__da=self.__salary*(20/100)
        self.__hra=self.__salary*(10/100)
        self.__pf=self.__salary*(5/100)
        self.__ns=self.__salary+self.__da+self.__hra-self.__pf

    def ShowEmployee(self):
        print("============Employee Data============")
        print("Employee ID : ",self.__id)
        print("Name : ",self.__name)
        print("Salary : ",self.__salary)
        print("DA : ",self.__da)
        print("HRA : ",self.__hra)
        print("PF : ",self.__pf)
        print("Net Salary : ",self.__ns)

S1=Employee()
S1.GetEmployee()
S1.GetSalary()
S1.ShowEmployee()