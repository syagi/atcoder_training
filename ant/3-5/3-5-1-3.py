
def dfs(v, t, f):
    if v == t: return f
    used[v] = True
    for to in SNS[v]:
        if not used[to] and SNS[v][to] > 0:
            d = dfs(to ,t, min(f, SNS[v][to]))
            if d > 0:
                SNS[v][to] -= d
                SNS[to][v] += d
                return d
    return 0

N,G,E = map(int,input().split())

# 友達関係。最終ノードを1つ追加
SNS = [ {} for _ in range(N+1)]
P = list(map(int, input().split()))

for p in P:
    SNS[p][N] = 1
    SNS[N][p] = 0

for _ in range(E):
    a,b = map(int,input().split())
    SNS[a][b]=1
    SNS[b][a]=1

flow = 0
while True:
    used = [False] * (N+1)
    if dfs(0, N, 1) == 0: break
    flow += 1

print(flow)
