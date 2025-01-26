s=input()
m=1
c=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c=c+1
    else:
        m=max(c,m)
        c=1
m=max(m,c)
print(m)