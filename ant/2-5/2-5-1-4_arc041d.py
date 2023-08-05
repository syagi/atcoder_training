import sys
sys.setrecursionlimit(100000)

from collections import defaultdict

N,M = map(int,input().split())

Graph = defaultdict(list)

results  = [[0 for _ in range(N)] for _ in range(N)]
Corrects = [[0 for _ in range(N)] for _ in range(N)]

Branches = []
for i in range(M)
    a,b,c = input().split()
    a = int(a)-1
    b = int(b)-1
    Graph[a].append(b)
    Graph[b].append(a)
    if c=='r':
        Corrects[a][b]=1
        Corrects[b][a]=1
    else:
        Corrects[a][b]=-1
        Corrects[b][a]=-1
    Branches.append([a,b]) 
    
def dfs(src, col, step):
    global results, check
    if steps[src] < 0:
        steps[src]=step
    elif abs(step-steps[src])%2:
        # 奇数閉路
        print("Yes")
        exit()
    
    ret=True
    for dest in Graph[src]:
        if results[src][dest]==0:
            results[src][dest]=col
            results[dest][src]=col
            if results[src][dest]!=Corrects[src][dest]:
                # 色が違う
                return False
            ret &= dfs(dest, -col, step+1)
    return ret

ans = False

for i in range(N):
    for j in [1, -1]:
        # init
        steps = [-1 for _ in range(N)]
        for src,dest in Branches:
            results[src][dest]=0
            results[dest][src]=0
        ans |= dfs(i,j,0)

if ans:
    print('Yes')
else:
    print('No')
