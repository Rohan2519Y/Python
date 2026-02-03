# List(sequence)
# - Collection which store hetrogeneous data
# - mutable in nature
#   means one can edit/delete, append elements of list
# - others all same as tuple(index,sliding,......)
# - to create a list
#   - list() constructor
#   - []
#   ex
#     L=list()
#        or
#     L=list()
# 
#   L=[1,2,3,4]
#   L=list(1,2,3,4)
# 
# Functions/////////////////////////////////////////////////////////////////////////////////////////////////
# append(object)
# append object @ end
# insert(position,object)
# remove (this remove from the object)
# pop()  --remove the last element
# pop(index)  --remove element according to index specified
# extend(object)  --add multiple elements
# clear()  --clear all elements
# copy()  --create deep copy
# deep copy
# shallow copy
# index(object,[si],[ei])
# count(object,[si],[ei])
# reverse()
# sort()
# 
# 



##########################################################################################################################################
# L=[4,5,6,7,'Gwalior',34,(23,45,67),[23,45,67]]
# L=[4,53,26,7,34,82]
# print(L)
# del L[5]
# L[6]='hello'
# L.append('Usa')
# L.insert(2,'Pune')
# L.remove("Gwalior")
# L[7].remove(45)
# L[6]=list(L[7])   --convert the tuple into list
# L.extend([1,2,3,4])
# T=L
# T[5]='Morena'
# T=L.copy()
# T[5]='Morena'
# L.sort()
# L.sort(reverse=True)
# print(L)


# n=int(input("Enter Number : "))
# city=[]
# for i in range(n):
#     c=input("Enter City : ")
#     city.append(c)
# print(city)


# L=[23,45,87,23,56,87,45,12]
# for i in range(L.count(45)):
#     L.remove(45)
# print(L)


# L=[[100,'Pepsi',90],[200,'Fanta',120],[300,'7up',140],[400,'Limka',10]]
# for i in L:
#     if i[2]>100:
#         print(i)


L=[12,65,76,45,34,23,78,65,12]
D=[]
for i in L:
    if (DICTL.count(i)>1):
        if i not in D:
            D.append(i)
print(D)