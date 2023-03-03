s1=[""]+list(input())
s2=[""]+list(input())

# dp[i][j] si[:i]とs2[:j]の距離
dp = [[0] * len(s2) for _ in range(len(s1))]

for i in range(1,len(s1)):
    dp[i][0]=i

for j in range(1,len(s2)):
    dp[0][j]=j

for i in range(1,len(s1)):
    for j in range(1,len(s2)):
        if s1[i]==s2[j]:
            dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
        else:
            dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)

print(dp[-1][-1])