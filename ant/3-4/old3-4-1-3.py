INF=10**10

# dfs S:訪問済集合(bit) v:現在地 
def solve(S,v,dp):
    if dp[S][v] != INF:
        # 訪問済み:w
        return dp[S][v]
    if S==(1<<V)-1 and v==0:
        # 探査完了
        return 0
    
    res = INF
    for u in range(V):
        if S>>u & 1 == 0 :
            res = min(res, solve(S|1<<u, u, dp)+G[v][u])
    dp[S][v] = res
    return res

V,E = map(int,input().split())
if E==0:
    print(-1)
    exit(0)

G=[[INF]*V for _ in range(V)]
for _ in range(E):
    s,t,d = (map(int,input().split()))
    G[s][t] = d

#dp[s][i]: iにいてsまで訪問した時のコストmin
dp = [[INF]*V for _ in range(1<<V)]

# 出発点がどこでも最小コストは同じ
ans = solve(0,0,dp)
if ans==INF:
    print(-1)
else:
    print(ans)