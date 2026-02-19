# lambda function/lambda exp
# --------------------------

# - anonymous function(fucntion without name) 
# - single liner function
# - syntax
#       <object>=lambda (parameters):<expression>
# Example
#       A=lambda a,b:a+b
#       K=A(3,5)
#       print(K)
# 
# Comprehension
# -------------
# if()
#       <true>  if(exp) else <false>
# 
# for
#       <var> for <var> in <collection>
# 
# 
# 
# 



# A=lambda a,b:a+b
# K=A(3,4)
# print(K)

# 5/9(F - 32)
# C=lambda f:(f-32)*5/9
# F=C(45)
# print("%.2f"%F)


# a=10
# b=20
# K=a if(a>b) else b
# K="A is Largest" if (a<b) else b
# print(K)


# a=10
# b=20
# c=30
# K="A is Largest" if (a>b and a>c) else "B is Largest" if(b>a and b>c) else "C is Largest"
# print(K)

# num=int(input("Enter Percentage : "))
# K="Grade A" if num<100 and num>80 else "Grade B" if num<79 and num>60 else "Grade C" if num<59 and num>40 else "Grade D"
# print(K)

# K=[i for i in range(1,11)]
# print(K)

# L1=[1,2,3,4]
# L2=[1,2,3,4]
# K=[L1[i]+L2[i] for i in range(len(L1))]
# print(K)

# K=lambda a,b,c:a if(a>b and a>c) else b if(b>c and b>a) else c
# t=K(1,2,3)
# print(t)

# K=lambda s,e: [chr(i) for i in range(ord(s),ord(e)+1)]
# j=K('a','x')
# print(j)

# L=['Gwalior','Indore','Bhopal']
# Search=lambda c:[print(i,": ","True") if (c in i) else print(i,":","False") for i in L]
# Search('or')

# def fact(n):
#     p=1
#     while(n>1):
#         p=p*n
#         n=n-1
#     return p

# L=[5,6,7,8,4]
# search=lambda value_list:[fact(i) for i in value_list]
# print(search(L))