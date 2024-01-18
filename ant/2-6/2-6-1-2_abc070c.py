import functools
import math

N=int(input())

t=[]
for _ in range(N):
    t.append(int(input()))


lcm=functools.reduce(math.lcm, t)

print(lcm)