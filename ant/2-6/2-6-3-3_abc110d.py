import math
MOD=10**9+7

def combr(n,r):
    return math.comb(n+r-1,r)

def factorization(n):
    result=[]
    tmp=n
    for i in range(2,int(n**0.5)+1):
        if tmp%i==0:
            cnt=0
            while tmp%i==0:
                cnt +=1
                tmp//=i
            result.append([i,cnt])
        if tmp==1:
            break
    else:
        result.append([tmp,1])
    if result==[]:
        result.append([n,1])
    return result

N,M=map(int,input().split())

f=factorization(M)

ans=1
for p,k in f:
    if p==1:
        continue
    ans *= combr(N,k)

print(ans%MOD)