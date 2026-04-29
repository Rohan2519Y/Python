# function
# --------
# - to divife a large program in a small module
# - one can call function any time any where in a program multiple times
#   thus it provides reusablity of code
# 
# syntax
# def <function name> (args):
# =========
# =========
# =========
# =========
# return value
# 
# default args
# def call(a,b,c=10):
# only trailing args are default
# 
# def call(*j):unlimited arg
# 
# 
# import myfile
# from myfile import sqrt, factorial
# 
# 
# 
# call by value
# in this tech. actual arg copied their values in formal arg and whatever changes will make in formal args will not affect the values of actual args
# 
# 
# 
# call by reference 
# in this tech. actual arg copied their address in formal arg and whatever changes will make in formal args will not affect the reference of actual args 
# 
# 

# def SimpleInterest(p,r,t):
#     s=p*r*t/100
#     return s

# print(SimpleInterest(100,200,3))


# def geteven(L):
#     E=[]
#     for i in L:
#         if i%2==0:
#             E.append(i)
#     return E

# L=[1,2,3,4]
# T=geteven(L)
# print(T)


# def getHexa(L):
#     E=[]
#     for V in L:
#         E.append(hex(V)[2:])
#     return ''.join(E)
# L=[123,34,54]
# T=getHexa(L)
# print(T)


# def removeChar(S,C):
#     return S.replace(C,'')

# T=removeChar('eoeienhe','e')
# print(T)


# def add_tag(i,tag):
#     L=('<',i,'>',tag,'</',i,'>')
#     return ''.join(L)
    

# T=add_tag('i','Python')
# print(T)



# def insert_string_middle(tag,value):
#     le=len(tag)//2
#     L=tag[:le]+value+tag[le:]
#     return L

# T=insert_string_middle('{{}}','Python')
# print(T)

# def insert_end(value):
#     return value[-2:]*4

# T=insert_end('Python')
# print(T)



# def hex_to_color(color):
#     L=[]
#     for i in range(len(color)-1):
#         if i % 2 == 0:
#             L.append(color[i:i+2])

#     return tuple(L)

# T= hex_to_color('ABCDEF')
# print(T)