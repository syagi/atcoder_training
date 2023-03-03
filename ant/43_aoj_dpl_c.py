N,W=map(int,input().split())

v=[]
w=[]

for i in range(N):
    vi,wi=map(int,input().split())
    v.append(vi)
    w.append(wi)

# dp[i][j] : i種類で重さjまで詰める最適解
dp = [ [0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        if j < w[i]:
            # 入らない
            dp[i+1][j]=dp[i][j]
        else:
            # max(そのまま, 1個詰める)
            dp[i+1][j]=max(dp[i][j],dp[i+1][j-w[i]]+v[i])

print(dp[N][W])