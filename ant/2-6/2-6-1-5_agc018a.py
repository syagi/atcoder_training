import functools
import math

N,K=map(int,input().split())

a = list(map(int,input().split()))

gcd_a=functools.reduce(math.gcd, a)

max_a=max(a)

if( K<=max_a and K%gcd_a==0 ):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
