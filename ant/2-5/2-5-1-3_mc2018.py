N=int(input())

parents=[]
siz=[1]*N

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
        siz[y]+=siz[x]
        siz[x]=siz[y]
        parents[root_x]=root_y

def same(x,y):
    return root(x)==root(y)

for i in range(N):
    a=int(input())-1
    unite(i,a)

max_size=max(siz)
if max_size%2==0:
    print(max_size//2)
else:
    print("-1")
    exit()
