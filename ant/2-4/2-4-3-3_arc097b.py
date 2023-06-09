N,M=map(int,input().split())

P=list(map(int,input().split()))
# Union Findで同じrootを持つ数字群はいつかソートできる
# よって、本来の位置とのsameが取れた数

parents=[]
for i in range(N):
    parents.append(i)

def root(x):
    if(parents[x]!=x):
        parents[x]=root(parents[x])
    return parents[x]

def unite(x,y):
    root_x = root(x)
    root_y = root(y)
    if (root_x!=root_y):
        parents[root_x]=root_y

def same(x,y):
    return root(x)==root(y)

for _ in range(M):
    x,y=map(int,input().split())
    unite(x-1,y-1)

ans=0
for i in range(N):
    if(same(P[i]-1,i)):
        ans+=1

print(ans)