# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1163&lang=jp
import math

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

while(True):
    M,N = map(int,input().split())
    if M==0 and N==0:
        break

    S = 0
    T = M+N+1
    G = [{} for _ in range(T+1)]
    INF = 10**18

    for x in range(M):
        G[S][x+1] = 1
        G[x+1][S] = 0

    for y in range(N):
        G[y+M+1][T] = 1
        G[T][y+M+1] = 0
    
    # データの途中で改行されることを考慮
    B = []
    while len(B)<M:
        B += list(map(int,input().split()))

    R = []
    while len(R)<N:
        R += list(map(int,input().split()))

    # 共に割り切れる組み合わせに枝を張る
    for i in range(M):
        for j in range(N):
            if math.gcd(B[i],R[j])>1:
                G[i+1][j+M+1]=1
                G[j+M+1][i+1]=0

    flow = 0
    while True:
        used = [False] * (T+1)
        f = dfs(S, T, INF)
        if f == 0:
            break
        flow += f
    print(flow)