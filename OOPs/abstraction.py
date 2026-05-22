# Abstract Class
# - the main property of abstract class is that 
#   one can not instantiate its object
#
# Abstract Methods
# - they have no body structure
# - & they must be redefine in derive class to achieve run time polymorphism
# - must be define in abstract class
# - 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


###############################################################
from abc import ABC, abstractmethod

# class Animal(ABC):   #ABSTRACT CLASS
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         super().sound()
#         print("Dog")

# class Cat(Animal):
#     def sound(self):
#         super().sound()
#         print('Cat Meows')


# D=Dog()
# D.sound()
# C=Cat()
# C.sound()

################################################################################
# RTP / Late Binding / Dynamic Binding
# class Student(ABC):
#     @abstractmethod
#     def get(self):
#         pass

#     @abstractmethod
#     def show(self):
#         pass

# class Bsc(Student):
#     def get(self):
#         self.__rollno=input("Enter Roll No :")
#         self.__name=input("Enter Name :")
#         self.__p=int(input("Enter P Marks :"))
#         self.__c=int(input("Enter C Marks :"))
#         self.__m=int(input("Enter M Marks :"))

#     def show(self):
#         print(self.__rollno, self.__name, self.__p, self.__c, self.__m,)

# T=Bsc()
# T.get()
# T.show()



#__repr__#####################################################
class Student:
    def getStudent(self):
        self.rollno=input("Enter Roll Number : ")
        self.name=input("Enter Number : ")
    def __repr__(self):
        return f"Name : {self.name}, Roll Number : {self.rollno}"
    def __str__(self):
        return f"Name : {self.name}, Roll Number : {self.rollno}"
    
S=Student()
S.getStudent()
print(S.__str__)
print(S.__repr__)