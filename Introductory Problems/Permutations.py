n=int(input())
c=1
z=2
if n==2 or n==3:
    print("NO SOLUTION")
elif n==4:
    print(2,4,1,3)
else:
    for i in range(1,n+1,2):
        print(i,end=' ')
    for i in range(2,n+1,2):
        print(i,end=' ')