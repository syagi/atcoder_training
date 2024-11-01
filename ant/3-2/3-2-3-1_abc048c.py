N,x = map(int,input().split())
a=list(map(int,input().split()))

ans=0
if a[0]>x:
    ans=a[0]-x
    a[0]=x
for i in range(1,N):
    sum=a[i-1]+a[i]
    if sum<=x:
        continue
    elif a[i]>sum-x:
        a[i]-=sum-x
    else:
        a[i]=0
        #a[i-1]-=sum-x-a[i]
    #print(a)
    ans+=sum-x

print(ans)