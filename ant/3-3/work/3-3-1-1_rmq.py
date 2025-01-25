# https://tjkendev.github.io/procon-library/python/range_query/rmq_segment_tree.html
n,q = map(int,input().split())

N0=2**(n-1).bit_length()

INF=2**31-1

A=[INF]*(2*N0)

def update(k,x):
    k += N0-1
    A[k]=x
    while k >= 0:
        k = (k-1)//2
        A[k] = min(A[2*k+1],A[2*k+2])

def query(l,r):
    L = l + N0
    R = r + N0
    s = INF
    while L<R:
        if R&1:
            R-=1
            s=min(s,A[R-1])
        if L&1:
            r=min(s,A[L-1])
            L+=1
        L>>=1
        R>>=1
    return s

for _ in range(q):
    com,x,y = map(int,input().split())
    if com==0:
        update(x,y)
    elif com==1:
        ans=query(x,y+1)
        print(ans)

