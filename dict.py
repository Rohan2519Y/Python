# dict
# --------------

# - a collection which store data using to constraints
# {key:value}
# key: it must be unique value(int/string/alphanumeric)
# value: hetrogenious
# 
# - use to read data randomly using keys
# - does not support indexing and slicing
#   becos data can be read only with the help of keys
# - does not allow concatination(+) and repetation(*) operator
# - does not support ==,<,>,>=,<= operator
# - support in operator to search keys
# - one can create dict using
#   -{}
#   -dict{}
# -mutable in nature
# 
# 
# 
# Methods
# -------
# setdefault(key,value)
# if specified key does not exist it will insert key and values in dict
# if key exist the it will the return the existing key and value
# 
# keys() will return all the keys in a dict
# values() will return all the values in a dict
# items() return both keys and values
# clear() clear the dict
# copy() create nwe copy of dict
# get(key,message) this fucntion return the value of specified key 
#                  if key does not exist it will return specified message
# fromkeys(sequence,,default_value) will generate dict using sequence
# - sequence elements are the keys
# - and their will be default_value
# pop(key) remove the values of specified key
# popitem() remove the last record
# update()
# set()



# D={100:'Deepak',200:'Pankaj',300:'Nitin',400:'Shankar'}
# D[500]='Alia'
# D[200]='Ambani'
# del D[300]
# print(D)
# print(D[200])




# D={100:{'Name':'Deepak','P':23,'C':67,'M':80},
#    200:{'Name':'Pankaj','P':67,'C':37,'M':20},
#    300:{'Name':'Nitin','P':24,'C':97,'M':84}}
# print(D[100]['Name'],D[100]['P'],D[100]['C'],D[100]['M'])
# print(100 in D)


# D={'Name':'Deepak','P':23,'C':67,'M':80}
# R=D.setdefault('Y',25)
# print(D)
# print(R)


# D={'Name':'Deepak','P':23,'C':67,'M':80}
# R=D.keys()
# print(R)
# for k in D.keys():
#     print(k,D[k])


# D={'Name':'Deepak','P':23,'C':67,'M':80}
# R=D.values()
# print(R)
# for k in D.values():
#     print(k)


# D={'Name':'Deepak','P':23,'C':67,'M':80}
# R=D.items()
# print(R)
# for T in R:
#     print(T[0],T[1])


# D={'Name':'Deepak','P':23,'C':67,'M':80}
# R=D.get("A","Not Found")
# R=D.get("P","Not Found")
# print(R)


# S=['BJP','INC','SP','AAP']
# D=dict.fromkeys(S,0)
# print(D)


# D={300:{'name':'Ajay1','P':89,'C':59,'M':86},100:{'name':'Ajay2','P':89,'C':59,'M':86},200:{'name':'Ajay3','P':89,'C':59,'M':86}}
# K=D.pop(200)
# print("Deleted : ",K)
# print(D)


# D={300:{'name':'Ajay1','P':89,'C':59,'M':86},100:{'name':'Ajay2','P':89,'C':59,'M':86},200:{'name':'Ajay3','P':89,'C':59,'M':86}}
# K=D.popitem()
# print("Deleted : ",K)
# print(D)


# D={300:{'name':'Ajay1','P':89,'C':59,'M':86},100:{'name':'Ajay2','P':89,'C':59,'M':86},200:{'name':'Ajay3','P':89,'C':59,'M':86}}
# N={400:{'name':'Ajay1','P':89,'C':59,'M':86},100:{'name':'Ajay3','P':89,'C':59,'M':86},200:{'name':'Ajay3','P':89,'C':59,'M':86}}
# D.update(N)
# print(D)


# D=[['12','adfa']]
# print(dict(D))


dic={1:30,2:10,3:20}
temp={}
for i in range(len(list(dic))):
    print((dic.items)[i])