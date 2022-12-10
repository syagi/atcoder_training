n=int(input())

X=[]
pairs=[]
for _ in range(n):
    x,w = map(int,input().split())
    X.append(x)
    pairs.append([x-w,x+w])

pairs.sort(key=lambda x:[x[1],x[0]])

ans=0
for l,r in pairs:
    tmp=0
    for x in X:
        if l<=x and x<=r:
            tmp+=1
    ans=max(ans,tmp)

print(ans)