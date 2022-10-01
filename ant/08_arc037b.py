from pydoc import resolve, visiblename
from re import S


N,M = map(int,input().split())

path=[[] for _ in range(N+1)]
for i in range(M):
    u,v = map(int,input().split())
    path[u].append(v)
    path[v].append(u)

visited = [False] * (N+1)
ans=0
def dfs(src,dest):
    if visited[dest]:
        return False
    
    visited[dest]=True
    ret=True
    for next in path[dest]:
        if next != src:
            ret &= dfs(dest,next)
    return ret

for n in range(1,N+1):
    if not visited[n]:
        if dfs(0,n):
            ans+=1
print(ans)