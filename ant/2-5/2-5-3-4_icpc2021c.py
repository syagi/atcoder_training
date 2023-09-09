
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

while(1):
    n,m = map(int,input().split())
    if(n==0 and m==0):
        exit()
    
    parents=[]
    for i in range(n):
        parents.append(i)
    branches=[]
    for i in range(m):
        s,t,c = map (int,input().split())
        branches.append([s-1,t-1,c])

    branches.sort(key=lambda x: x[2])

    ans=[]
    for b in branches:
        if not same(b[0], b[1]):
            unite(b[0], b[1])
            ans.append(b[2])

    import statistics
    print(statistics.median(ans))
