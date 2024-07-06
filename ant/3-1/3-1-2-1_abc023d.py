N=int(input())

balloons=[]
h_max = 0
s_max = 0
for _ in range(N):
    h,s = map(int,input().split())
    h_max=max(h,h_max)
    s_max=max(s,s_max)
    balloons.append([h,s])

def check(x):
    times=[]
    for h,s in balloons:
        if h > x:
            return False
        else:
            t = (x-h)//s
            times.append(t)
    times.sort()
    
    for i in range(N):
        if i > times[i]:
            return False
    return True

high = h_max*s_max*N
low  = 0

while abs(high-low) > 1:
    mid = (high+low) // 2
    if check(mid):
        high = mid
    else:
        low = mid

print(high)