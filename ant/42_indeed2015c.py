N,M = map(int, input().split())

# dp[i][j][k] a=i,b=j,c=k の年収
# 102は 0の場合に使用する帳尻合わせ
dp = [[[0]*102 for _ in range(102)] for _ in range(102) ]

for _ in range(N):
    a,b,c,w = map(int,input().split())
    dp[a][b][c]=max(dp[a][b][c],w)

for i in range(101):
    for j in range(101):
        for k in range(101):
            dp[i][j][k]=max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1],dp[i][j][k])

for _ in range(M):
    a,b,c = map(int,input().split())
    print(dp[a][b][c])