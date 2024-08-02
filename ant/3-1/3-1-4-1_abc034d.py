N,K=map(int,(input().split()))

W=[]
P=[]
for _ in range(N):
    w,p = map(int,input().split())
    W.append(w)
    P.append(p)

ok=0.0
ng=100.0
while (abs(ok-ng) > 10**-9):
    mid=(ok+ng)/2
    A=[]
    for i in range(N):
        A.append( W[i]*(P[i]-mid) )
    A.sort(reverse=True)
    ans=0.0
    for i in range(K):
        ans+=A[i]
    
    if ans<0:
        ng=mid
    else:
        ok=mid

print(ok)
