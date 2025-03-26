n=int(input("enter the number of rows"))
x=1
for i in range(1,n+1):
    for a in range(1,i+1):
        print(x,end=" ")
        x=x+1
    print()
