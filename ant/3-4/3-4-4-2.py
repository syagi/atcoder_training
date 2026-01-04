# https://drken1215.hatenablog.com/entry/2022/12/17/014915

# 行列積
def mulmatmod(a,b,md):
    m,n = len(a), len(b[0])
    res = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(len(b)):
                res[i][j] +=a[i][k] * b[k][j]
                res[i][j] %=md
    return res

# 行列の累乗
def powmatmod(a,p,md):
    m = len(a)

    res = [[0]*m for _ in range(m)]
    
    # 単位行列で初期化
    for i in range(m):
        res[i][i]= 1

    while p>0:
        if p & 1:
            res = mulmatmod(res,a,md)
        a = mulmatmod(a,a,md)
        p >>=1
    return res   

def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a

A,B,M = map(int,input().split())

C=[[10,1],[0,1]]

g = gcd(A,B)

# a_k+1 = 10*a_k + 1 の A項
fA=powmatmod(C,A,M)[0][1]

# a_k+1 = 10^g*a_k+1 の B/g項
D=[[powmatmod(C,g,M)[0][0],1],[0,1]]
fB_fD=powmatmod(D, B//g, M)[0][1]

print(fA*fB_fD%M)