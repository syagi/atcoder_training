
# 別海 https://github.com/syagi/atcoder_training/blob/main/46_abc153e.py

H,N = map(int,input().split())

A=[]
B=[]

for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

# dp[i][j]: i種類で HP j を倒す
INF = 10**10
dp = [[INF for _ in range(H+1)] for _ in range(N+1)]
dp[0][0]=0
for i in range(N):
    for j in range(H+1):
       # 魔法iを使わない
       dp[i+1][j]=min(dp[i+1][j],dp[i][j]) 
       # 魔法iを使う
       # ダメージA[i]が入るので、 dp[i+1][j+A[i]] or dp[i+1][H] (H<j+A[i]) を更新
       dp[i+1][min(j+A[i],H)]=min(dp[i+1][min(j+A[i],H)],dp[i+1][j]+B[i])

print(dp[N][H])