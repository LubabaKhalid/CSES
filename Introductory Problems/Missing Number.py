n=int(input())
l=list(map(int,input().split()))
if n not in l:
    print(n)
else:
    
    l=sorted(l)
    for i in range(1,n):
        if i!=l[i-1]:
            print(i)
            break