N,M=map(int,input().split())
A=[]
for _ in range(N):
    a=int(input())-1
    A.append(a)

# nums[m][n] 種類mが n区画までに何個あるか
nums = [[0]*(N+1) for _ in range(M)]
for i in range(M):
    for j in range(N):
        if A[j]==i:
            nums[i][j+1] = nums[i][j] + 1
        else:
            nums[i][j+1] = nums[i][j] 

INF=1<<60
# dp[s] 種類sまで並べたときの最小コスト
dp = [INF] * (1<<M)
dp[0] = 0

for S in range(1<<M):
    done = 0
    # 個数の更新
    for i in range(M):
        if S & (1<<i):
            done += nums[i][N]
    
    for i in range(M):
        if S & (1<<i):
            continue

        T = S|(1<<i)
        # 種類 i の総数
        total_i = nums[i][N]
        # 種類 i のうち動かさないやつ
        remain_i = nums[i][done + total_i] - nums[i][done]
        # 種類 i のうち動かすやつ
        remove = total_i - remain_i
        dp[T] = min(dp[T], dp[S] + remove)

print(dp[(1<<M)-1])