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

def SimpleInterest(p,r,t):
    s=p*r*t/100
    return s

print(SimpleInterest(100,200,3))