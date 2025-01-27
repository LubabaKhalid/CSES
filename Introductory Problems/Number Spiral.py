n=int(input())
for _ in range(n):
    x,y=map(int,input().split())
    m=max(x,y)
    m2=m*m
    if m%2==1:
        if y==m:
            print(m2-x+1)
        else:
            print(m2-y+1)
    else:
        if x==m:
            print(m2-y+1)
        else:
            print(m2-x+1)
    