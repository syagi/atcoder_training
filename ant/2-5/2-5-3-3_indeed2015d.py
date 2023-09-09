import sys
sys.setrecursionlimit(10000)
H,W = map(int,input().split())
Sx,Sy = map(int,input().split())
Gx,Gy = map(int,input().split())

parents=[]
N=(H+2)*(W+2)

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

P=[[0]*(W+2)]
ans=0
for i in range(H):
   pi=list(map(int,input().split())) 
   P.append([0]+pi+[0])
   ans += sum(pi)
P.append([0]*(W+2))

# print(P)
branches=[]
for i in range(1,H+1):
    for j in range(1,W+1):
        current=i*W+j
        # 上
        branches.append([current-W,current,P[i-1][j]*P[i][j]*-1])
        # 下
        branches.append([current+W,current,P[i+1][j]*P[i][j]*-1])
        # 左
        branches.append([current-1,current,P[i][j-1]*P[i][j]*-1])
        # 右
        branches.append([current+1,current,P[i][j+1]*P[i][j]*-1])

branches.sort(key=lambda x: x[2])
# print(branches)

for b in branches:
    if not same(b[0],b[1]):
        unite(b[0],b[1])
        ans += b[2]*-1

print(ans)