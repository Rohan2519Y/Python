
class Student:
    def GetStudent(self):
        self.__rollno=input("Enter Roll Number : ")
        self.__name=input("Enter Name : ")

    def GetMarks(self):
        self.__p=input("Enter Physics Marks : ")
        self.__c=input("Enter Chemistry Marks : ")
        self.__m=input("Enter Maths Marks : ")

    def ShowMarks(self):
        print("Roll Number : ",self.__rollno)
        print("Name : ",self.__name)
        print("Physics Marks : ",self.__p)
        print("Chemistry Marks : ",self.__c)
        print("Maths Marks : ",self.__m)

    @staticmethod
    def Heading():
        print("-------------Data---------------")

    def Search(self,rollno):
        if(self.__rollno==rollno):
            self.ShowMarks()
            return True
        return False

L=[]
n=int(input("Enter Number : "))
for i in range(n):
    S1=Student()
    S1.GetStudent()
    S1.GetMarks()
    L.append(S1)

rollno=input("Enter Roll Number U want to Search : ")

Student.Heading()
for STD in L:
    found=STD.Search(rollno)
    if(found):break

if not found :
    print("Student Not Found")