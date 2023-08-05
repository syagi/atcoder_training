n,k=map(int,input().split())

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

path=[set() for _ in range(n)]

for _ in range(k):
    line = list(map(int,input().split()))
    src = line[1]-1
    dst = line[2]-1
    if line[0]==1:
        path[src].add((dst,line[3]))
        path[dst].add((src,line[3]))
        # print(costs)
    else:
        costs = dijkstra(src,path)
        print(costs[dst])