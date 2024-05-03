l,r = map(int,input().split())

sqrt_r=int(r**0.5)
isprime = [False,False] + [True] * (sqrt_r-1)

# 素数列挙
for p in range(2,sqrt_r+1):
    if not isprime[p]:
        continue
    for k in range(p*p,sqrt_r+1,p):
        isprime[k]=False
 
# print(isprime)
ans=0
# 順次素因数分解
for n in range(l,r+1):
    # print(n)
    if n==1:
        continue
    factors=0
    while n%2==0:
        factors+=1
        n//=2
    f=3
    while f*f<=n:
        factors+=1
        n//=f
        f+=2
    if n!=1:
        factors+=1
    # print(factors)
    if isprime[factors]:
        ans+=1

print(ans)