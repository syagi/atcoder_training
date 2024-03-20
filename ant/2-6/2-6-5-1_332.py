import math

A,B=map(int,input().split())

# √B以下の素数を篩う
upper=int(B**0.5)+1
isprime = [True] * upper

# A以上B以下の素数pを篩う
isprime2 = [True] * (B-A+1)

for p in range(2,upper):
    if not isprime[p]:
        continue

    # p以外のpの倍数を排除
    q=p+p
    while q*q<=B:
        isprime[q]=False
        q+=p
    
    # Aより大きいpの倍数の最小値
    # (-x)%y = y-x%y
    # よって、 A+(-A)%p = A+p-A%p = p + (A-A%p) で、pの倍数になる
    start = A+(-A)%p
    if start == p :
        # p自身を排除しない
        start = p+p

    # AとBの間で篩
    q = start
    while q<=B:
        isprime2[q-A]=False
        q+=p

print(sum(isprime2))