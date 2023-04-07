N,M,L,X = map(int,input().split())


a=list(map(int,(input().split())))

inf = 10**10
# dp[i][j] : i番目の燃料タンクをつかってjにたどり着く最小周回.(たどり着けない場合はinf)

dp = [[inf]*M for _ in range(N+1)]
dp[0][0]=1

for i in range(N):
    for j in range(M):
        if j-a[i]>=0:
            # 周回増やさないで到着
            dp[i+1][j] = min(dp[i][j],dp[i][j-a[i]])
        else:
            # 何周かしないとダメ
            tmp = dp[i][(j-a[i])%M]+abs(j-a[i])//M+1
            dp[i+1][j] = min(dp[i][j],tmp)

if dp[N][L]<X:
    ans="Yes"
else:
    ans="No"

print(ans)
