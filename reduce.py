# reduce###################################################################################################
# reduce(function,seq,[initial value])

import functools
# L=[32,45,37,96]
# K=functools.reduce(lambda a,b:a+b,L)
# K=functools.reduce(lambda a,b:a+b,L,0)
# K=functools.reduce(lambda a,b:a+b,L,500)
# print(K)

L=[['India Gate',1000,800],['Netscafe',1000,800],['Juice',1000,800]]
total_cost=functools.reduce(lambda a,b:a+b[1],L,0)
actual_cost=functools.reduce(lambda a,b:a+b[2],L,0)
print("Total Cost : ",total_cost)
print("Actual Cost : ",actual_cost)
print("Final Amount : ",total_cost-actual_cost)