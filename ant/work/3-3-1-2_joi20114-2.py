N = int(input())

A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(N)]
# 番号なので0始まりにする
B = [b-1 for b in B]

segTree=[0]*(2*N+1)

def segfunc(x,y):
    return max(x,y)

def update(k,x):
    k += N
    segTree[k]=x
    while k >= 0:
        k //= 2
        segTree[k] = segfunc(segTree[2*k+1],segTree[2*k])

def query(l,r):
    L = l + N
    R = r + N
    s = 0
    while L<R:
        if R&1:
            s=segfunc(s,segTree[R-1])
        if L&1:
            s=segfunc(s,segTree[L])
            L+=1
        L>>=1
        R>>=1
    return s

for b in B:
    t = query (0,b)
    update(b, A[b]+t)

ans = (sum(A) - query(0,N)) *2
print(ans)