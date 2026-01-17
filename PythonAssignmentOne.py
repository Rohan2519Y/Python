# a=0
# e=0
# i=0
# o=0
# u=0
# str=input("Enter String : ")

# for j in list(str):
#     if j=='a' or j=='A':
#         a+=1
#     elif j=='e' or j=='E':
#         e+=1
#     elif j=='i' or j=='I':
#         i+=1
#     elif j=='o' or j=='O':
#         o+=1
#     elif j=='u' or j=='U':
#         u+=1

# print("A :",a,"\nE :",e,"\nI :",i,"\nO :",o,"\nU :",u)



# str=input("Enter Text : ")
# c=False
# for i in str:
#     if(i=='['):
#         print(end=' ')
#         c=True
#         continue
#     elif(i==']'):
#         c=False
#         continue
#     if(c):
#         print(i,end='')



# for i in range(65,91):
#     if i<78:
#         print(chr(i),end=' ')
#     else:
#         if(i==78):print()
#         print(chr(i),end=' ')



# str=input("Enter Text : ").lower()
# cl=""
# for ch in str:
#     if ch.isalpha() or ch.isspace():
#         cl+=ch

# w=cl.split()
# c=0

# for i in range(len(w)):
#     if w[i] == "wood":
#         c=c+1

# print("Count : ",c)



T="Hello World!"
K=sorted(T)
L="".join(K)
print(L)



#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# copy=60
# price=24.95-(24.95*0.4)
# print("Total : ",(copy*price)+3+((copy - 1) * 0.75))

# current=14
# go=535
# print("Answer :",(current+go)%24,": 00")

# amt=int(input("Enter Input : "))
# d=amt//100
# print("Dollar : ",d)
# amt=amt%100
# q=amt//25
# print("Quartz : ",q)
# print("Remaining : ",amt)

# a=int(input("Enter First Number : "))
# b=int(input("Enter Second Number : "))
# c=int(input("Enter Third Number : "))
# print("Max : ",max(a,b,c))
# print("Min : ",min(a,b,c))
# print("Average : ",(a+b+c)/3)

# str=input("Enter Text : ")
# c=0
# for i in 'aeiou':
#     if i in str.lower():
#         c+=1
# print("there are",c,"different vowels in the string")

