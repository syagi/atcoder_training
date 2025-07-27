N,M = map(int,input().split())
N,M = map(int,input().split())

# 自分より前に何羽いるか
G=[0]*N

for _ in range(M):
    x,y = map( lambda x:int(x)-1, input().split())
    G[y] |= 1<<x

# 部分集合のトポロジカルソートパターン数
dp = [0] * 2**N
dp[0]=1

for i in range(1<<N):
    for j in range(N):
        if i>>j&1 or i&G[j]:
            continue
        dp[i|1<<j] += dp[i]

print(dp[-1])