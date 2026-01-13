#1###################################################
# str=input("Enter Text : ")
# print("Answer : ",len(str))



#2###################################################
# str=input("Enter Text : ")
# w={}
# for i in str:
#     if i in w:
#         w[i]+=1
#     else:
#         w[i]=1
# print(w)



#3###################################################
# str=input("Enter Text : ")
# l=len(str)
# if l<2:
#     print(str)
# elif l==2:
#     print(str,str,sep='')
# else: 
#     print(str[:2],str[l-2:],sep='')



#4###################################################
# str=input("Enter Text : ")
# w=str[0]
# for i in range(1,len(str)):
#     if str[0] == str[i]:
#         w+='$'
#     else:
#         w+=str[i]
# print("Answer : ",w)



#5###################################################
# str1=input("Enter Text 1 : ")
# str2=input("Enter Text 2 : ")
# print(str1.replace(str1[:2],str2[:2]),str2.replace(str2[:2],str1[:2]))



#6###################################################
# str=input("Enter Text : ")
# if len(str)<3:
#     print(str)
# elif str[-3:]=='ing':
#     print(str,'ly',sep='')
# else:
#     print(str,"ing",sep='')



#7###################################################
# str=input("Enter Text : ")
# if 'good' in str:
#     print(str.replace('good','poor'))
# elif 'not' in str:
#     print(str.replace(str[str.find('not'):str.find('poor')],''))



#8###################################################
# arr=['abdc','jhk','gyjygujy']
# long=arr[0]
# for i in range(len(arr)):
#     if len(arr[i])>len(long):
#         long=arr[i]
# print("Longest Word : ",long,"\nLength of the Longest Word : ",len(long))



#9###################################################
# str='hello'
# i=int(input("Enter Index : "))
# print(str.replace(str[i],'',1))



#10###################################################
# str1=input("Enter Text1 : ")
# str2=input("Enter Text2 : ")
# print(str2[:1],str1[1:-1],str2[-1:],sep='')



#11###################################################
# str=input("Enter Text : ")
# w=''
# for i in range(len(str)):
#     if i%2!=0:
#         w+=''
#     else:
#         w+=str[i]
# print(w)



#12###################################################
# str=input("Enter Text : ")
# w={}
# for i in str.split():
#     if i in w:
#         w[i]+=1
#     else:
#         w[i]=1
# print(w)



#13###################################################
# str=input("Enter Text : ")
# print("Lower : ",str.lower())
# print("Upper : ",str.upper())



#14###################################################
# str=input("Enter Text : ").split(',')
# w=[]
# for i in str:
#     if i in w:
#         ''
#     else:
#         w.append(i)
# print(sorted(w))



#15###################################################
def add_tag(i,a):
    print()
add_tag(2,3)