n=int(input())
a=list(map(int,input().split()))

ans=-1

for l in range(n):
    a_min=a[l]
    for r in range(l,n):
        a_min=min(a_min,a[r])
        ans=max(ans,a_min*(r-l+1))

print(ans)