# class TwoNum:
#     def getValues(self):
#         self.__x=int(input("Enter X : "))
#         self.__y=int(input("Enter Y : "))

#     def putValues(self):
#         print(self.__x,self.__y)

#     def add(self, T):
#         R=TwoNum()
#         R.__x=self.__x+T.__x
#         R.__y=self.__y+T.__y
#         return R

# T1=TwoNum()
# T2=TwoNum()
# T1.getValues()
# T2.getValues()
# T1.putValues()
# T2.putValues()
# T3=T1.add(T2)
# T3.putValues()

######################################################################
class Time:
    def getTime(self,h,m,s):
        self.__h=h
        self.__m=m
        self.__s=s

    def putTime(self):
        print(self.__h,self.__m,self.__s)

    # def __add__(self, T):
    def add(self, T):
        R=Time()
        R.__h=self.__h+T.__h
        R.__m=self.__m+T.__m
        R.__s=self.__s+T.__s

        R.__m=R.__m+(R.__s//60)
        R.__s=R.__s%60

        R.__h=R.__h+(R.__m//60)
        R.__m=R.__m%60

        d=R.__h//24
        print("DAYS :",d)
        R.__h=R.__h%24

        return R

T1=Time()
T2=Time()
T1.getTime(10,50,70)
T2.getTime(100,500,700)
T1.putTime()
T2.putTime()
T3=T1.add(T2)
T3.putTime()