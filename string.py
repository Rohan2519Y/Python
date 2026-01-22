# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""Strings"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# group of characters
# ex india, atal
# -strings are immutable in nature
# -support various operators like
#   +(concat) *(repeatation)
# - support indexing and slicing

# slicing
#          [[si]:[ei]:[diff]]
#          ei-1

# Methods of string object
# capitalize()  --capital only first word first letter
# title()  --capital all words first letter
# upper()  --upper all the letter to uppercase
# lower()  --upper all the letter to lowercase
# swapcase()  --convert upper to lower and vice versa
# index(substring,[si],[ei])  return the position of specified substring
#                             if specified substr is not exist in string it will generate Exception
# find(substring,[si],[ei])
# rfind(substring,[si],[ei])
# count(str,[si],[ei])  --count how many times a character comes
# endswith(str,[si],[ei]) --return true if string end with specified str otherwise false
# startswith(str,[si],[ei]) --return true if string start with specified str otherwise false
# ljust(width,fill_char)
# rjust(width,fill_char)
# center(width,fill_char)
# strip([str]) --remove leading and trailing spaces
# rstrip([str]) --remove leading and trailing spaces from right side
# lstrip([str]) --remove leading and trailing spaces from left side
# split([chr],[n])
# rsplit([chr],[n])
# partition()
# replace(str1,str2,[n])  --replace str1 with str2
#                         [n] number of replacement
# islower() --give true or false
# isupper() --give true or false    //GWALIOR --true
# istitle() --//Gwalior   --true
# isalnum() --alphabet and number allowed    //Gwalior   --true
# isdigit() --//"1234"   --true  //"12.5" --false
# isnumeric()
# isspace()
# len()
# max()
# min()
# sum()
# all()    --if nothing is present then false //Non,'',0
# any()    --if one entry is present then true
# sorted()   --sorted(k,reverse=True)
# .format()  j="sum of {} and {} is {}".format(a,b,c)

# x='abc'
# y='def'
# z=x+y
# print(z)

# x='   hello   '
# k=x*10
# print(k)

# K="AMIT"
# J="AMAR"
# T=K>J
# print(T)

# K="AMIT"
# J="AMAR"
# T="MIT" in K
# print(T)

# K="AMIT"
# print(K[2])

# x="This is Text Program"
# print(x[1:5])
# print(x[:5])
# print(x[6:])
# print(x[:])
# print(x[6:-5])
# print(x[::-1])

# x="GWALIOR"
# print(x[-2])
# for i in x:
#     print(i)
# for i in x:
#     print(i,ord(i))

# for i in range(65,91):
#     print(chr(i),end=' ')

# k="hello World to to everyone"
# x=k.capitalize()
# print(x)
# x=k.title()
# print(x)
# x=k.upper()
# print(x)
# x=k.lower()
# print(x)
# x=k.swapcase()
# print(x)
# x=k.index("to")
# print(x)
# x=k.find("to")
# print(x)

# x="heloo nkasddd heloo"
# t=x.rfind("heloo")
# print(t)

# i=0
# while(True):
#     i=k.find('to',i)
#     if(i==-1):break
#     print(i)
#     i=i+1

# x=k.find("to",3,9)
# print(x)

# x="Ram Narayan Sharma"

# si=x.find(' ')
# ei=x.find(' ',si+1)

# print(x[si+1:ei])

# x="Gwalior"
# t=x.count('l',3)
# print(t)

# x="Gwalior"
# t=x.count('l',3,4)
# print(t)

# x="Jaipur"
# t=x.endswith('pur',)
# print(t)

# x="Jaipur"
# t=x.endswith('pur',3)
# print(t)

# x="Jaipur"
# t=x.endswith('ip',1,4)
# print(t)

# k=['Gwalior','Bhopal','Rampur']
# for i in k:
#     if i.endswith('pur'):
#         print(i)

# k=['Gwalior','Bhopal','Rampur']
# for i in k:
#     if i.startswith('Ram'):
#         print(i)

# k=['Gwalior','Bhopal','Rampur','Indore']
# for i in k:
#     if i.count('io')>0 or i.count('do')>0:
#         print(i)

# k=['Gwalior','Bhopal','Rampur','Indore']
# for i in k:
#     if 'io' in i or 'do' in i:
#         print(i)

# k="MALYALAM"
# j=k.ljust(10,"#")
# print(j)

# k="MALYALAM"
# j=k.rjust(10,"#")
# print(j)

# k="1234567890"
# j=k[6:].rjust(10,"*")
# print(j)

# k="    hello    "
# j=k.strip()
# print(j)

# k="----hello----"
# j=k.strip("-")
# print(j)

# k="a,b,c,d,e"
# t=k.split(',')
# print(t)

# k="a,b,c,d,e"
# t=k.split(',',2)
# print(t)

# k="Hello how are Hello"
# t=k.partition('how')
# print(t)

# K="the man the machine the python"
# t=K.replace("the",'that')
# print(t)

# K="the man the machine the python"
# t=K.replace("the",'that',2).replace("that","the",1)
# print(t)

# t=['a','b','c','d']
# m=''.join(t)
# print(m)

# t="Ram Kumar Hari Mohan Sharma"
# k=t.split()
# for i in range(len(k)-1):
#     print(k[i][0],end='.')
# print(k[len(k)-1])

# k="python program:best scripting for science"
# l=k.rfind(' ')
# str=k[0:l]+' data'+k[l:]
# print(str)
# for i in t:
#     if(i=='science'):
#         print('data',end=' ')
#     print(i,end=' ')

# word=input("Enter Text : ")
# k="python program:best scripting for science"
# str=k.replace(word,'')
# print(str)

# k="python    program    best    scripting   for    science"
# l=k.split(' ')
# str=''
# for i in l:
#     if i != '':
#        str=str+i+' '

# print(str)

# k="python    program    best    scripting   for    science"
# l=k.split()
# str=" ".join(l)
# print(str)


a=10
b=10
c=a+b
# j="sum of {0} and {0} is {0}".format(a,b,c)
j="{0:<15.2f}\n{1:^15.2f}\n{2:15.2f}".format(a,b,c)
print(j)