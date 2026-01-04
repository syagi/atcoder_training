
# 備忘 https://lab-brains.as-1.co.jp/enjoy-learn/2023/07/50258/

# 行列積
def mulmat(a,b):
    m,n = len(a), len(b[0])
    res = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(len(b)):
                res[i][j] ^=a[i][k] & b[k][j]
    return res

# 行列の累乗
def powmat(a,p):
    m = len(a)

    res = [[0]*m for _ in range(m)]
    
    # 単位行列で初期化
    for i in range(m):
        res[i][i]= (1<<32)-1

    while p>0:
        if p & 1:
            res = mulmat(res,a)
        a = mulmat(a,a)
        p >>=1
    return res   

K,M = map(int,input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))


# Aの転置行列（vector)
matA = []
for a in A[::-1]:
    matA.append([a])

# 1行目が C、2行目以降が K-1 * K-1 の単位行列
matC = [C]
# 2行目以降
for i in range(K-1):
    matC.append([0]*K)
    matC[i+1][i] = (1<<32) -1

if M < K:
    # 計算するまでもないやつ
    print(A[M-1])
else:
    # 解説通りの演算
    # M-1乗後、Aのvectorとの積
    print(mulmat(powmat(matC, M-K), matA)[0][0])