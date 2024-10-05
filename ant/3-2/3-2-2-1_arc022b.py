N=int(input())

A=list(map(int,input().split()))

r=0
flavors=set()
ans=0

for l in range(N):
    while r<N:
        if A[r] in flavors:
            break
        else:
            flavors.add(A[r])
            r+=1
    ans=max(ans, r-l)
    flavors.discard(A[l])

print(ans)