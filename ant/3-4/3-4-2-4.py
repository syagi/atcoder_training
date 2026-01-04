N=int(input())
X=list(map(int,input().split()))
X.sort()

INF=1<<60
# dp[S] S個倒したあと何か投げるか
dp= [INF]*(1<<N)
dp[(1<<N)-1] = 0

# あと1枚から順に走査
for bit in reversed(range(1<<N)):
    for i in range(16):
        # i番目の座標を狙う場合
        

print(dp[0])