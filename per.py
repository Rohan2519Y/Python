import itertools as it
import random as rand

# K=it.permutations('ABCD')
# K=it.permutations([3,4,5])
# print(list(K))

# K=it.groupby(sorted([1,2,3,4,2,3,4,1]))
# for (i,v) in K:
#     t=list(v)
#     print(i,t,len(t))

# K=int(rand.random()*5)+1
# K=int(rand.random()*8999)+1000
# print(K)

# print(rand.randrange(1000,9000)) do not include
# print(rand.randdict(1000,9000)) include

# L=[1,2,3,4]
# K=rand.choice(L)
# print(K)

# L=[1,2,3,4]
# rand.shuffle(L)
# print(L)

# L=[('Peter',45),('Deepu',34),('Chetan',22),('Harry',65)]
# def call(T):
#     return T[0]
# K=sorted(L,key=call)
# K=sorted(L,key=lambda T:T[1])
# print(K)

# L=[1,2,3,4]
# print(rand.sample(L,k=2))

# comb=it.combinations_with_replacement([1,2,3],3)
# for i in comb:
#     print(i)