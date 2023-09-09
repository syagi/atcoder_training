
V,E = map(int,input().split())
parents=[]
for i in range(V):
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

branches=[]

for i in range(E):
    s,t,w = map (int,input().split())
    branches.append([s,t,w])

branches.sort(key=lambda x: x[2])

sum=0
for b in branches:
    if not same(parents[b[0]], parents[b[1]]):
        unite(parents[b[0]], parents[b[1]])
        sum += b[2]

print(sum)


