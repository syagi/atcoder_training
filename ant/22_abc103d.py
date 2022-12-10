N,M=map(int,input().split())

pairs=[]

for _ in range(M):
    a,b=map(int,input().split())
    pairs.append([a,b])

pairs.sort(key=lambda x:[x[1],x[0]])

tmp=-1
ans=0

for l,r in pairs:
    if(tmp<=l):
        tmp=r
        ans +=1
print(ans)