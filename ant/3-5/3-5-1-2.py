
def dfs(v, t, f):
    if v == t: return f
    used[v] = True
    for to in FullEdge[v]:
        if not used[to] and FullEdge[v][to] > 0:
            d = dfs(to ,t, min(f, FullEdge[v][to]))
            if d > 0:
                FullEdge[v][to] -= d
                FullEdge[to][v] += d
                return d
    return 0

N,M,d = map(int,input().split())

# 飛行機だけの有向辺
Edge = []

# 人数が変わる時刻
TIMES = [ set() for _ in range(N)]

for _ in range(M):
    u, v, p, q, w = map(int,input().split())
    u -= 1
    v -= 1
    Edge.append(((u,p), (v,q+d), w))
    TIMES[u].add(p)
    TIMES[v].add(q+d)

# 待機まで考慮した有向辺
FullEdge = []
V = 0
id = {}
for u in range(N):
    Vs = V
    for t in sorted(TIMES[u]):
        id[(u,t)] = V
        FullEdge.append({})
        if V > Vs:
            # 移動無しの場合(同位置の未来へは無限流量)
            FullEdge[V-1][V] = float('inf')
            FullEdge[V][V-1] = 0
        V += 1

for src, dest, cap in Edge:
    x = id[src]
    y = id[dest]
    if y in FullEdge[x]:
        FullEdge[x][y] += cap
    else:
        FullEdge[x][y] = cap
        FullEdge[y][x] = 0

flow = 0
while True:
    used = [False]*V
    f = dfs(0, V-1, float('inf'))
    if f == 0:
        break
    flow += f
print(flow)