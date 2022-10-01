import sys
sys.setrecursionlimit(1000000)


H,W = map(int,input().split())

c=[ input() for _ in range(H) ]

for i in range(H):
    for j in range(W):
        if c[i][j]=="s":
            si,sj=i,j
        elif c[i][j]=="g":
            gi,gj=i,j

visited=[[False]*W for _ in range(H)]

def dfs(x,y):
    visited[x][y]=True

    for i,j in [[x, y+1],[x,y-1],[x-1,y],[x+1,y]]:
        if (i<0 or H<=i or j<0 or W<=j):
            continue
        elif c[i][j]=="#":
            continue
        elif not visited[i][j]:
            dfs(i,j)

dfs(si,sj)

if visited[gi][gj]:
    print("Yes")
else:
    print("No")
