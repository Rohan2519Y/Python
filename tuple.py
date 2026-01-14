# tuple 
# -is the collection / sequence which holds data hetrogeneous in nature
# -its immutable in nature
# -use to store days/months/fruits/birth date/cities/states/etc 
# -Operators
#   +(concat)   
#   *(repeat)   
#   >,<,==,!=,<=,>=   
#   in, not in   
# -to create tuple we can use
#   tuple() constructor
#   ()
# 
# Example
#   T=() or T=tuple()
# -indexing and slicing is use to read data from tuple
# 
# Methods of Tuple
# count(object)
# index(object,[si],[ei])
# find out the index of specified object
# will generate exception if object does not exist

# T=(12,23,34,45)
# T=tuple((12,23,34,45))
# print(T)
# print(T[0])

# T=(12,12.3,'Gwalior')
# print(T[2][2:5])

# T=(12,12.3,'Gwalior',(1,2,3,4))
# print(T[3][3])
# print(T[3][1:3])

# T1=(12,1,2,3,4)  
# T2=(12,13,24,63,74)
# print(T1>T2)        # CHECK ONLY FIRST ELEMENT if not equal first element
# print(T1==T2)        # CHECK ALL ELEMENTS

# T1=(12)     #NOT TUPPLE
# T1=(12,)     

T=(78,25,578)
l=T.index(74)
print(l)