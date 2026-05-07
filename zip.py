# zip
# use to merge the corresponding elements of sequences
# zip(S1, S2, S3, .........)
# 
# 
# 
# 
# 
# 
# 
# 

# L1=[1,2,3,4]
# L2=[1,2,3,4]
# T=list(zip(L1,L2))
# print(T)

# we can use only one time not multiple times

# A=[1,2,3,4]
# B=[1,2,3,4]
# C=[]
# M=list(zip(A,B))
# for i in M:
#     C.append(sum(i))
# print(C)


# A=['MP','UP','HR','PB']
# B=['Bhopal','Lucknow','Chandigarh','Chandigarh']
# C=['600','700','800','300']
# M=list(zip(B,C))
# D=dict(zip(A,M))
# print(D)