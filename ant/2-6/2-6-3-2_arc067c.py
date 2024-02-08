
def prime_list(n):
    primes=[]
    for i in range(2,n+1):
        for j in range(2, int(n**0.5)+1):
            if i==j:
                continue
            if i%j==0:
                break
        else:
            primes.append(i)
    return primes

N=int(input())
MOD=10**9+7

primes=prime_list(N)
facts=[0]*len(primes)

for i in range(2,N+1):
    for j in range(len(primes)):
        if i%primes[j]==0:
            tmp=i
            while tmp%primes[j]==0:
                facts[j]+=1
                tmp //= primes[j]
#print(primes)
#print(facts)
ans=1
for i in facts:
    ans *= i+1

print(ans%MOD)