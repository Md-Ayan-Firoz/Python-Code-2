n=int(input("Enter The Number: "))
a=0
b=1
for i in range(0,n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c

