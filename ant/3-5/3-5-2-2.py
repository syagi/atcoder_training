# https://atcoder.jp/contests/abc091/tasks/arc092_a

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


N = int(input())
S = 0
T = 2*N+1
G = [{} for _ in range(T+1)]
INF = 10**18

# 始点から red
for x in range(N):
    G[S][x+1] = 1
    G[x+1][S] = 0

# blue から終点
for y in range(N):
    G[y+N+1][T] = 1
    G[T][y+N+1] = 0

# Red
A=[]
B=[]
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

# Blue
C=[]
D=[]
for _ in range(N):
    c,d = map(int,input().split())
    C.append(c)
    D.append(d)


# ペアになり得る所だけ枝を張る
for i in range(N):
    for j in range(N):
        if A[i]<C[j] and B[i]<D[j] :
            G[i+1][j+N+1]=1
            G[j+N+1][i+1]=0

# print(G)

flow = 0
while True:
    used = [False] * (T+1)
    f = dfs(S, T, INF)
    if f == 0:
        break
    flow += f

print(flow)