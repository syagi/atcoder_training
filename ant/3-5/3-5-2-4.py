# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2480&lang=en
import sys

sys.setrecursionlimit(10**6)

def dfs(v,t,f):
    if v==t: return f
    used[v] = True
    for to in G[v]:
        if not used[to] and G[v][to] > 0:
            d = dfs(to, t, min(f, G[v][to]))
            if d > 0:
                G[v][to] -= d
                G[to][v] += d
                return d
    return 0


N,M = map(int,input().split())
S = 0
T = N+M+1
G = [{} for _ in range(T+1)]
INF = 10**18

# 始点から左群へ
for x in range(N):
    G[S][x+1] = 1
    G[x+1][S] = 0

# 右群から終点へ
for y in range(M):
    G[y+N+1][T] = 1
    G[T][y+N+1] = 0

# グラフ生成
for i in range(1,N+1):
    line = list(map(int,input().split()))
    K = line[0]
    B = line[1:1+K]
    for b in B:
        b += N
        G[i][b] = 1
        G[b][i] = 0

flow = 0
while True:
    used = [False] * (T+1)
    f = dfs(S, T, INF)
    if f == 0:
        break
    flow += f

# 2部グラフのサイズがMならBobの勝ち
if(flow==M):
    print("Bob")
else:
    print("Alice")
