# map()##########################################################################################################
# map(function,sequences)
# 
# 
# 
# 


# L=[1,2,3,4,5]
# K=list(map(lambda v:v*v,L))
# print(K)

# L1=[1,2,3,4,5]
# L2=[1,2,3,4,5]
# K=list(map(lambda v,j:v+j,L1,L2))
# print(K)

# L=[['Fanta',45,2],['Pepsi',30,10],['Red Bull',120,10]]
# K=list(map(lambda i:i[1]*i[2],L))
# print(sum(K))

def sumList(a,b):
    return a+b

L1=[1,2,3,4,5]
L2=[1,2,3,4,5]
K=list(map(sumList,L1,L2))
print(K)