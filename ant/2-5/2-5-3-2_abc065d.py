import sys
sys.setrecursionlimit(10000)
N = int(input())
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

cities=[]
branches=[]

for i in range(N):
    x,y = map (int,input().split())
    cities.append([x,y,i])

cities.sort()
for i in range(N-1):
    w = min(abs(cities[i+1][0]-cities[i][0]),abs(cities[i+1][1]-cities[i][1]))
    branches.append([cities[i][2],cities[i+1][2],w])

cities.sort(key=lambda x: x[1])
for i in range(N-1):
    w = min(abs(cities[i+1][0]-cities[i][0]),abs(cities[i+1][1]-cities[i][1]))
    branches.append([cities[i][2],cities[i+1][2],w])

branches.sort(key=lambda x: x[2])
sum=0
for b in branches:
    if not same(b[0],b[1]):
        unite(b[0],b[1])
        sum += b[2]

print(sum)
