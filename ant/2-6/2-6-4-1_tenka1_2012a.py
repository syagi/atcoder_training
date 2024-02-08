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

n=int(input())
ans=len(prime_list(n-1))

print(ans)