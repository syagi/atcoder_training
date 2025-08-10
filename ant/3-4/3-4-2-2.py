
# 現在の配置mapに対し、位置nに置いて矛盾が起きるか
def check(map,n):
    # 縦の評価
    if 0 < n//5 < 4:
        # 上下が配置済
        if (map>>(n-5) & 1) ^ (map>>(n+5) & 1):
            return False
    # 横の評価
    if 0 < n%5 < 4:
        # 左右が配置済
        if (map >> (n-1) & 1) ^ (map >> (n+1) &1):
            return False
    return True

MOD = 10**9 + 7
fixed ={ } # 固定された数の位置
free = []  # 未定の位置

for i in range(5):
    for j,x in enumerate(map(int,input().split())):
        if x > 0:
            fixed[x] = i*5+j
        else:
            free.append(i*5+j)

MAP = {0:0}

# dp[S]: 集合Sを配置した時点で矛盾していなパターン数
dp = [0] * (1<<len(free))
dp[0]=1

# 小さい数から配置評価
for n in range(1,26):
    # 既に置かれた数
    if n in fixed:
        for S in MAP:
            if not dp[S]:
                # 既に矛あり
                continue
            if check(MAP[S], fixed[n]):
                MAP[S] |= 1 << fixed[n]
            else:
                # この時点で矛盾あり
                dp[S] = 0
    # これから置く数
    else:
        new = {}
        for S in MAP:
            if not dp[S]:
                # 既に矛盾あり
                continue
            # 未配置のマスを順次評価
            for i in range(len(free)):
                if S>>i & 1:
                    continue
                if check(MAP[S], free[i]):
                    dp [S | 1<<i] += dp[S]
                    dp [S | 1<<i] %= MOD
                    # 配置後の5x5
                    new [S | 1<<i] = MAP[S] | 1<<free[i]
        MAP = new

print(dp[-1])
