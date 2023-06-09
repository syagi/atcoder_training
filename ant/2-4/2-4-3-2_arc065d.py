N,K,L = map(int,input().split())

parents=[]

def root(x,i):
    # print("..before_parents[",i,"][",x,"]",parents[x][i])
    if(parents[x][i]!=x):
        parents[x][i]=root(parents[x][i],i)
    # print("..after_parents[",i,"][",x,"]",parents[x][i])
    return parents[x][i]

def unite(x,y,i):
    root_x = root(x,i)
    # print("..root_",x,":",root_x)
    root_y = root(y,i)
    # print("..root_",y,":",root_y)
    if (root_x!=root_y):
        parents[root_x][i]=root_y
    #print("..",parents)

for i in range(N):
    parents.append([i,i])

# print(parents)
#road
for _ in range(K):
    p,q = map(int,input().split())
    # print(p-1,q-1)
    unite(p-1,q-1,0)

#train
for _ in range(L):
    r,s = map(int,input().split())
    unite(r-1,s-1,1)

# 全ノードのrootを整形
for i in range(N):
    root(i,0)
    root(i,1)

#print(parents)
import collections

# collectionはlistをつかえないのでtupleに
cities=[(parents[i][0],parents[i][1]) for i in range(N)]
ans=collections.Counter(cities)

print(*[ans[cities[i]] for i in range(N)])
