n,m,x = map(int,input().split())

c=[]
a=[]
for i in range(n):
    ca=list(map(int,input().split()))
    c.append(ca[0])
    a.append(ca[1:])

ans=10**10

for i in range(2**n):
    cost=0
    skill=[0]*m

    for shift in range(n):
        if (i>>shift & 1)==1:
            cost+=c[shift]
            for j in range(m):
                skill[j]+=a[shift][j]
    if x<=min(skill):
        ans=min(ans,cost)

if ans==10**10:
    print(-1)
else:
    print(ans)
