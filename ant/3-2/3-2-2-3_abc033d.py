import math
from bisect import bisect_left,bisect_right

N=int(input())

points=[]
pi90=math.pi/2
pi360=math.pi*2

for _ in range(N):
    x,y=map(int,input().split())
    points.append((x,y))

obtuses=0 # 鈍角
rights=0  # 直角

# 角abcの各頂点を j, i, k として偏角で考える  
for i in range(N):
    rads=[]
    for j in range(N):
        if i!=j:
            dx=points[i][0]-points[j][0]
            dy=points[i][1]-points[j][1]
            rads.append(math.atan2(dy,dx)%pi360)
    rads.sort()
    for j in range(N-1):
        rads.append(rads[j]+pi360)
    for j in range(N-1):
        rad = rads[j]
        p1=bisect_left(rads, rad + pi90 - 1*10**(-9))
        p2=bisect_left(rads, rad + pi90 + 1*10**(-9))
        p3=bisect_left(rads, rad + math.pi)
        rights+=p2-p1
        obtuses+=p3-p2

actues = N*(N-1)*(N-2)//6 - obtuses - rights

print(actues, rights, obtuses)