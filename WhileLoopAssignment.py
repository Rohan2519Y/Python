# a=int(input("Enter Number : "))
# i=0
# while(i<=a):
#     i=i+a

# print("Sum : ",i)



# n=5
# size=n*2-1
# i=0
# while(i<size):
#     j=0
#     while(j<size):
#         value=n-min(i,j,size-i-1,size-j-1)
#         print(value,end=" ")
#         j+=1
#     print()
#     i+=1



n = 5

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print(i + 1, end=" ")
        else:
            print(" ", end=" ")
    print()
