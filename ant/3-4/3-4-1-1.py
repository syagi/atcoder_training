N=int(input())

A=[]
for _ in range(N):
    a = list(map(int,input().split()))
    A.append(a)

INF = 10**18

#dp[s][i]: iにいてsまで訪問した時のコストmin
dp = [[INF]*N for _ in range(1<<N)]

# スタート時のコストは0:w
dp[1<<0][0]=0

# dp走査
for s in range(1<<N):
    if not (s & 1):
        continue
    for i in range(N):
        if not (s & 1<<i):
            continue
        if dp[s][i] == INF:
            continue

        a,b,c = A[i]
        for j in range(N):
            if i==j:
                continue
            p,q,r = A[j]
            new_s = s | (1<<j)
            itoj = abs(p-a)+abs(q-b)+max(0,r-c)
            dp[new_s][j] = min(dp[new_s][j], dp[s][i]+itoj)

# print(dp)

full = (1<<N)-1
ans = INF

p,q,r=A[0]
for i in range(N):
    a,b,c = A[i]
    # 一番短い帰り道
    candicate = dp[full][i] + abs(p-a) + abs(q-b) + max(0,r-c)
    ans = min(ans,candicate)

print(ans)