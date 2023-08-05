N,M=map(int,input().split())

roads=[ set() for _ in range(N)]

for i in range(M):
    f,t,c = map(int,input().split())
    # 目的地から先へは行けないので、目的地発のパスは作らない
    if(f!=N-1):
        roads[f].add((t,c))
    if(t!=N-1):
        roads[t].add((f,c))


from heapq import heappop, heappush
def dijkstra_e(src,path,d):
    # 時間の剰余で表を拡張 (costs[i][k] : node[i]到達時間%d = k となる最短時間)
    costs = [[-1]*d for _ in range(N)]
    # q: [(コスト,目的地)]
    q = [(0,src)]
    while q:
        c,v = heappop(q)
        if costs[v][c%d] !=-1:
            continue
        costs[v][c%d]=c
        for u, fee in path[v]:
            fee+=c
            if costs[u][fee%d]==-1:
                heappush(q, (fee, u))
    return costs

cost4=dijkstra_e(0,roads,4)
# print(cost4)
cost7=dijkstra_e(0,roads,7)
# print(cost7)

if (cost4[N-1][0]==-1):
    print(cost7[N-1][0])
elif (cost7[N-1][0]==-1):
    print(cost4[N-1][0])
else:
    print(min(cost4[N-1][0],cost7[N-1][0]))