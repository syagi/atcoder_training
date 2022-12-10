n,m=map(int,input().split())

c = list(map(int,input().split()))

ans=0
for coin in c.sort(reverse=True) :
    ans+=int(n/c)
    c%=coin

print(ans)