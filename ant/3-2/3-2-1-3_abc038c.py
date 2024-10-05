N=int(input())

A=list(map(int,input().split()))
A.append(-1)
l=0
r=0
ans=0

while l<N:
    while r<N and A[r]<A[r+1]:
        r+=1
    ans+=(r-l+1)
    l+=1
    r=max(l,r)

print(ans)
