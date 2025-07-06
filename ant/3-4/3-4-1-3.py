INF=10**10
V,E = map(int,input().split())
if E==0:
    print(-1)
    exit(0)

G=[[] for _ in range(V)]
for _ in range(E):
    s,t,d = (map(int,input().split()))
    G[s].append((t,d))

# print(G)
#dp[s][i]: iにいてsまで訪問した時のコストmin
dp = [[INF]*V for _ in range(1<<V)]

dp[1][0]=0

for i in range(1<<V):
    for j in range(V):
        if not i & (1<<j):
            continue
        for e in G[j]:
            next=e[0]
            if (i & (1<<next)):
                continue
            next_i=i|(1<<next)
            dp[next_i][next] = min(dp[next_i][next], dp[i][j]+e[1])

ans=INF
for i in range(V):
    for e in G[i]:
        if e[0]==0:
            ans=min(ans,dp[(1<<V)-1][i]+e[1])

if ans==INF:
    print(-1)
else:
    print(ans)