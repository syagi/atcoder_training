H,W,N=map(int,input().split())

C=[[] for _ in range(H)]

for i in range(H):
    C[i]=list(input())

for i in range(H):
    for j in range(W):
        if C[i][j]=='S':
            sy=i
            sx=j
            C[i][j]='.'
            break

import copy
from collections import deque

time = 0
for i in range(1,N+1):
    c=copy.deepcopy(C)
    dq = deque()
    dq.append([sy,sx,time])
    # print('s',sy,sx,time)
    c[sy][sx]='X'
    while dq:
        # print(dq)
        y,x,time=dq.popleft()
        # print(y,x,time)
        for ny,nx in [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]:
            if ny<0 or H<=ny or nx<0 or W<=nx :
                continue
            elif c[ny][nx]=='X':
                continue
            elif c[ny][nx]=='.':
                dq.append([ny,nx,time+1])
                c[ny][nx]='X'
            elif i==int(c[ny][nx]):
                sy=ny
                sx=nx
                time+=1
                # print('eat',sy,sx,time)
                break
            else:
                dq.append([ny,nx,time+1])
                c[ny][nx]='X'
        else:
            continue
        break

print(time)
