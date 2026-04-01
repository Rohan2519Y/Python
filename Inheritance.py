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
# 
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
class Student:
    def getStudent(self):
        self.__rollno=input("Enter Roll Number : ")
        self.__name=input("Enter Name : ")

    def showStudent(self):
        print(self.__rollno, self.__name)

class Bsc(Student):
    def getSubject(self):
        self.getStudent()
        self._p=int(input("Enter Physics Marks : "))
        self._c=int(input("Enter Chemistry Marks : "))
        self._m=int(input("Enter Maths Marks : "))

    def showSubjects(self):
        self.showStudent()
        print(self._p, self._c, self._m)

    def getTotal(self):
        t=self._p + self._c + self._m
        return t

class Result(Bsc):
    def getResult(self):
        self.getSubject()
        self.__total=self.getTotal()

    def showResult(self):
        self.showSubjects()
        print(self.__total)

S=Result()
S.getResult()
S.showResult()