N,W=map(int,input().split())

vw=[]
for _ in range(N):
    vw.append(list(map(int,input().split())))

dp = [ [0] * (W+1) for _ in range(N+1)]

for i, (v,w) in enumerate(vw):
    for j in range(W+1):
        dp[i+1][j]=dp[i][j]
        if j - w >= 0:
            dp[i+1][j]=max(dp[i+1][j], dp[i][j-w] + v)

print(dp[-1][-1])