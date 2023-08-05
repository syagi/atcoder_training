n,m,s,t = map(int,input().split())
s-=1
t-=1

yen_path    = [set() for _ in range(n)] 
sunuke_path = [set() for _ in range(n)] 

for _ in range(m):
    u,v,a,b = map(int,input().split())
    u-=1
    v-=1
    yen_path[u].add((v,a))
    yen_path[v].add((u,a))
    sunuke_path[u].add((v,b))
    sunuke_path[v].add((u,b))

from heapq import heappop, heappush

INF=10**16
def dijkstra(src,path):
    costs = [-1]*n
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

yen_costs=dijkstra(s,yen_path)
sunuke_costs=dijkstra(t,sunuke_path)
# print(yen_costs)
# print(sunuke_costs)

ans=[0 for _ in range(n)]
# n-1 年後から評価 
tmp_ans=INF
for i in reversed(range(n)):
    tmp_ans=min(tmp_ans,yen_costs[i]+sunuke_costs[i])
    ans[i]=tmp_ans

for i in range(n):
    print(10**15-ans[i])
