import functools
import math

n=int(input())

l=list(map(int,input().split()))

gcd=functools.reduce(math.gcd, l)

for i in range(1,gcd):
    if gcd % i ==0:
        print(i)
print(gcd)