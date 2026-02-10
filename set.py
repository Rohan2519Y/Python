
# - set is unordered list contains unique elements
# - set is hetrogeneous collection but one can not add index based object like tuple, list and dict
# - elements of sets is immutable but whole is mutable
# - does not support indexing and slicing
# - one can read data by loop
# - does not support +(concate) and *(repeat)
# - support >,<,<=,>=,==,!=,in,is
# - one can create set using set(),{}
# support all collection method - sum, len, sorted, any, all, min, max
# -method
#  add(object)
# clear()
# copy() - create deep copy
# discard(element)
# pop()
# remove(element)
# union(set)
# intersection(set)
# difference(set)
# issuperset(set)
# isdisjoint()
# 
# 







# t={1,2,3,4,5,6,7,8,9}
# for i in t:
#     print(i)

# t={1,2,3,4,5,6,7,8,9}
# # t.add(20)
# # t.discard(3)
# t.update({90})
# print(t)


t1={1,2,3,4,5,6,7,8,9}
t2={90,100}
t3=t1.union(t2)
print(t3)