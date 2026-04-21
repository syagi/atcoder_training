# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_7_A&lang=jp

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


X,Y,E = map(int,input().split())
S = 0
T = X+Y+1
G = [{} for _ in range(T+1)]
INF = 10**18

for x in range(X):
    G[S][x+1] = 1
    G[x+1][S] = 0

for y in range(Y):
    G[y+X+1][T] = 1
    G[T][y+X+1] = 0

for _ in range(E):
    x,y = map(int,input().split())
    x += 1
    y += X + 1
    G[x][y] = 1
    G[y][x] = 0

# print(G)

flow = 0
while True:
    used = [False] * (T+1)
    f = dfs(S, T, INF)
    if f == 0:
        break
    flow += f

print(flow)