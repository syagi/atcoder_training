N,K = map(int,input().split())

a = []
suma=[1]
tmp=0
for _ in range(N):
    ai=int(input())
    a.append(ai)
    tmp+=ai
    suma.append(tmp)


if sum(a)==K:
    print("1")
    exit()

inf = 11**10
# dp[i][j] : i日目にj回機嫌が良くなる最小勝利数
dp = [[inf] * (N+1) for _ in range(N+1)]

dp[0][0]=0
for i in range(1,N+1):
    dp[i][1]=1

# カンニング https://atcoder.jp/contests/arc057/submissions/37393899
for i in range(N):
    for j in range(i+1):
        dp[i+1][j]=min(dp[i+1][j], dp[i][j])
        # 今回勝利/今回試合 > 前回勝利/前回試合
        # dp[i+1][j+1]/sum(a[:i+1]) > dp[i][j]/sum(a[:i])
        # dp[i+1][j+1] > dp[i][j]/sum(a[:i])*sum(a[:i+1])
        # 整数に近似
        # dp[i+1][j+1] = dp[i][j]*sum(a[:i+1])//sum(a[:i]) + 1
        dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]*suma[i+1]//suma[i]+1)

ans = 1

for i in range(N, -1, -1):
    if dp[N][i] <= K:
        ans = i
        break

print(ans)
