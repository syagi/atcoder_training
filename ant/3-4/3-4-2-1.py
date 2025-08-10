N=int(input())
X=list(map(int,input().split()))
C=list(map(int,input().split()))
V=list(map(int,input().split()))

stock = [t :=0 ]
stock += [t := t + x for x in X]

# dpf[S][k] : 販売停止集合Sに対し、k個売却したときの最大得点
dpf = [ [-1] * (N+1) for _ in range(1<<N) ]

def f(S,k):
    if dpf[S][k] < 0:
        if S == (1<<N) -1 or k==0:
            # 全部販売停止 or 売却無し
            dpf[S][k] = 0
        else:
            # a: 売った財宝
            c,v,a = 0,0,[]
            # 全商品走査
            for i in range(N):
                if S >> i & 1:
                    # 販売停止中
                    continue
                c += C[i]
                v += V[i]
                a.append(i)
            if c <= stock[k]:
                dpf[S][k] = v
            else:
                res = 0
                for i in a:
                    res = max(res, f(S | 1<<i, k))
                dpf[S][k] = res
    return dpf[S][k]

# dp[S]:販売停止 S に対する最大得点
dp = [0] * (1<<N)
for S in range((1<<N) -1)[::-1]:
    k = N
    mindp = float('inf')
    for i in range(N):
        if S >> i & 1:
            continue
        k -= 1
        mindp = min(mindp, dp[S | 1<<i])
    dp[S] = max(f(S,k), mindp)
print(dp[0])