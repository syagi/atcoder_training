H,W = map(int,input().split())

c=[[] for _ in range(H)]

for i in range(H):
    c[i]=list(input())
    for j in range(W):
        if c[i][j]=='s':
            sy=i
            sx=j
        elif c[i][j]=='g':
            gy=i
            gx=j

from collections import deque

dq = deque()
time=0
dq.append([sy,sx,time])
c[sy][sx]='x'
time_g=H*W

while dq:
    y,x,time = dq.popleft()
    for ny,nx in [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]:
        if ny<0 or H<=ny or nx<0 or W<=nx :
            continue
        elif c[ny][nx]=='x':
            continue
        elif c[ny][nx]=='#':
            dq.append([ny,nx,time+1])
            c[ny][nx]='x'
        elif c[ny][nx]=='.':
            dq.appendleft([ny,nx,time])
            c[ny][nx]='x'
        elif c[ny][nx]=='g': 
            time_g = min(time,time_g)

if time_g<=2:
    print("YES")
else:
    print("NO")