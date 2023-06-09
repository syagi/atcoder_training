N,Q=map(int,input().split())

parents=[]

for i in range(2*N):
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
    w, x, y, z = map(int,input().split())
    x-=1
    y-=1
    if w==1:
#        print(w,x,y,z)
#        print(parents)
        if z%2==0:
            unite(x,y)
            unite(x+N,y+N)
        else:
            unite(x,y+N)
            unite(x+N,y)
#        print(parents)
    else:
#        print(w,x,y,z)
#        print(parents)
        if same(x,y):
            print("YES")
        else:
            print("NO")
