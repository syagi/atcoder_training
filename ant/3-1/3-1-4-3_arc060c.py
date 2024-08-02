N,A = map(int,input().split())

X = list(map(int,input().split()))

# dp[i][j][k] : i枚から j枚選んで 合計 k を作るバリエーション
dp =[[[ 0 for _ in range(50*50+1)] for _ in range(51) ] for _ in range(51)]

dp[0][0][0]=1

for i in range(N):
    for j in range(N):
        for k in range(50*50):
            if dp[i][j][k]>0:
                # 一枚増やしたけど使わない場合
                dp[i+1][j][k] += dp[i][j][k]
                # 一枚増やして使う場合
                dp[i+1][j+1][k+X[i]] += dp[i][j][k]

ans = 0
# 平均A (=合計 i*A) になる組み合わせの総数
for i in range(1,N+1):
    ans += dp[N][i][i*A]

print(ans)