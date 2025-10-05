# pypyだとMLE
N,M = map(int,input().split())

# C[i] : i番目のくじのバリエーション数
# Cost[i] : i番目のクジのコスト
# Idol[i][j] : i番目のくじのjパターンめの出目
# P[i][j] : i番目のくじのjパターン芽の確率
C,Cost = [], []
Idol, P = [],[]

for _ in range(M):
    c,cost = map(int,input().split())
    C.append(c)
    Cost.append(cost)
    i,p = [],[]
    for _ in range(c):
        a,b = map(int,input().split())
        i.append(a-1)
        p.append(b/100)
    Idol.append(i)
    P.append(p)

INF = 1 << 60

# dp[S] Sを持ってる状態でかかる最小費用
dp = [INF]*(1<<N)
dp[(1<<N)-1] = 0 # コンプリート

# あと1枚から順に走査
for bit in reversed(range(1<<N)):
    for i in range(M):
        # i番目のクジを考慮
        SUM = 0 # 合計コスト
        p = 0   # 合計確率
        for j in range(C[i]):
            if not 1<<Idol[i][j] & bit:
                # まだ引いていないアイドル
                SUM += dp[bit|1<<Idol[i][j]] * P[i][j]
                p += P[i][j]
        if p == 0:
            continue
        dp[bit] = min(dp[bit], (Cost[i]+SUM)/p)

print(dp[0])