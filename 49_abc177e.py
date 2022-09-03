N=int(input())
A=list(map(int,input().split()))

MAX=10**6*10

d=[0]*(MAX)

for i in range(2,MAX):
    if d[i]!=0:
        continue
    for k in range(1,10**6):
        if i*k<MAX:
            if d[i*k]==0:
                d[i*k]=i
        else:
            break

def fast_prime_fact(x):
    prime=[]
    while 1<x:
        prime.append(d[x])
        x//=d[x]
    return prime

pairwise=True
prime_used=[0]*(MAX)
for i in range(N):
    prime_list=fast_prime_fact(A[i])
    prime_set=set(prime_list)
    for j in prime_set:
        if prime_used[j]==1:
            pairwise=False
            break
        else:
            prime_used[j]=1

if pairwise:
    print("pairwise coprime")
    exit()

from math import gcd
g=A[0]

for i in range(1,N):
    g=gcd(g,A[i])

if g==1:
    print("setwise coprime")
else:
    print("not coprime")

