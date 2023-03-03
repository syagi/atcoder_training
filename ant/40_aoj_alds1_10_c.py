def lcs(X,Y):
    # dp[i][j]: i文字目までのXとj文字目までのYのLCS
    dp = [[0] * len(Y) for _ in range(len(X))]

    for i in range(1, len(X)):
        for j in range(1, len(Y)):
            if X[i] == Y[j]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1], dp[i-1][j])
    print(dp[-1][-1])

q = int(input())
for _ in range(q):
    x=[""]+list(input())
    y=[""]+list(input())
    lcs(x,y)