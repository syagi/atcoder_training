import sys

# デフォルトだとRE
sys.setrecursionlimit(10000)
N=int(input())

tree=[[] for _ in range(N)]

for i in range(N-1):
    u,v,w=map(int,input().split())
    u-=1
    v-=1
    tree[u].append((v,w))
    tree[v].append((u,w))

ans=[-1 for _ in range(N)]

# color は 0か1
def dfs(v, parent, color):
    ans[v]=color
    for edge in tree[v]:
        if edge[0]==parent:
            # 考慮済
            continue
        if edge[1]%2==1:
            # 奇数枝の場合色を反転
            dfs(edge[0], v, 1-color)
        else:
            dfs(edge[0], v, color)

dfs(0,-1,0)

for i in range(N):
    print(ans[i])
