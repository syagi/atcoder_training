N=int(input())

S=[0]
L=[0]
P=[0]
for _ in range(N):
    s,l,p = map(int,input().split())
    S.append(s)
    L.append(l)
    P.append(p)

M=int(input())
W=[]
w_max=0
for _ in range(M):
    w = int(input())
    W.append(w)
    w_max = max(w_max,w)

dp=[[-1 for _ in range(w_max+1)] for _ in range(N+1)]
dp[0][0]=0

for i in range(1,N+1):
    for j in range(w_max+1):
        dp[i][j] = max(dp[i][j],dp[i-1][j])
        for k in range(S[i],L[i]+1):
            if(j>=k):
                dp[i][j] = max(dp[i][j],dp[i][j-k]+P[i])

ans=[]
for i in range(M):
    if dp[N][W[i]]==-1:
        print("-1")
        exit()
    ans.append(dp[N][W[i]])

for i in range(M):
    print(ans[i])
