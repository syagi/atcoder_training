N,Q = map(int,input().split())

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

for _ in range(Q):
    p,a,b = map(int,input().split())
    if(p==0):
        unite(a,b)
    else:
        if(same(a,b)):
            print("Yes")
        else:
            print("No")
