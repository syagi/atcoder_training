import math

A,B,C=map(int,input().split())

def f(t):
    return A*t + B*math.sin(C*t*math.pi)

low = 0
high = 200
edge = 10 ** -9
mid = (high + low ) / 2 

while abs(100-f(mid))>edge:
    mid = (high + low ) / 2 
    if f(mid) < 100:
        low = mid
    else:
        high = mid

print(mid)
