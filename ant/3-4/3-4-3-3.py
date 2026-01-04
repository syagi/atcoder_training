MOD = 10 ** 9 + 7
N, X, Y, Z = map(int, input().split())

sz = X + Y + Z - 1
target = 1 << X - 1 | 1 << X + Y - 1 | 1 << sz
mask = (1 << sz) - 1
dp = [[0] * (1 << sz) for _ in range(2)]
crt = dp[0]
nxt = dp[1]
crt[0] = 1

for _ in range(N):
    for i in range(1 << sz):
        nxt[i] = 0
    for i in range(1 << sz):
        if not crt[i]: continue 
        ni = i << 1 | 1 
        for _ in range(10):
            if ni & target != target:
                nxt[ni & mask] += crt[i]
                nxt[ni & mask] %= MOD
            ni <<= 1
    crt, nxt = nxt, crt
print((pow(10, N, MOD) - sum(crt)) % MOD)
