# Exception Handling
# Exception are run time error
# 
# - try
# - except
# - finally -- EXECUTE AT LAST WHEATER AN ERROR OCCURED OR NOT
# - raise
# 
# try
#   captures series of errors at run time and throw it to the exception block where user can customize the error message
# 
# 
# 
# there are many classes 
# ex - 
#   top most exception class Exception(handle all python errors)
# 
# 
# - IndexError
# - ZeroDivison
# - ValueError
# - Exception
# 
# 
# 
# 
# 
# 
# 
# 
# 

# while(True):
#     try :
#         i = int(input("Input Integer Value : "))
#         break
#     except ValueError as E :
#         print("Error : ",E)


# Multiple Exception Block
# try : 
#     L = [5,7,8,9]
#     i = int(input("Enter Index : "))
#     print(L[i])
# except ValueError as e:
#     print("Value Error : ",e)
# except IndexError as e:
#     print("Index Error : ",e)
# except Exception as e:
#     print("Exception Error : ",e)


try :
    k = int(input("Enter Number : "))
    if not (k<=100 and k>=0):
        raise(Exception("Enter Correct Value"))
except Exception as E:
    print("Error :",E)