N,M,T = map(int,input().split())

A = list(map(int,input().split()))

path = [ set() for _ in range(N)]
rev_path = [ set() for _ in range(N)]

for i in range(M):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    path[a].add((b,c))
    rev_path[b].add((a,c))

#print(path)
#print(rev_path)

from heapq import heappop, heappush

def dijkstra(src,path):
    costs = [-1]*N
    # q: [(コスト,目的地)]
    q = [(0,src)]
    while q:
        c,v = heappop(q)
        if costs[v] !=-1:
            continue
        costs[v]=c
        for u, fee in path[v]:
            if costs[u]==-1:
                heappush(q, (c+fee, u))
    return costs

go_time=dijkstra(0,path)
back_time=dijkstra(0,rev_path)
#print(go_time)
#print(back_time)

ans=0
for i in range(N):
    if go_time[i]==-1 or back_time[i]==-1:
        continue
    ans = max(ans, A[i]*(T-go_time[i]-back_time[i]))

print(ans)