N=int(input())

P=list(map(int,input().split()))

dp=[[0] * (N*100+1) for _ in range(N+1)]

# dp[x][y] : x問でy点取れるか
dp[0][0]=1

for i,p in enumerate(P):
    for j in range(N*100+1):
        dp[i+1][j]=dp[i][j]
        if j>=p:
            dp[i+1][j]|=dp[i][j-p]

print(sum(dp[N]))
