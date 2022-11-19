R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())

c=[ [] for _ in range(R)]
for i in range(R):
    c[i]=list(input())

from collections import deque

dq = deque()
dq.append([sy-1,sx-1,0])
c[sy-1][sx-1]='#'

while dq:
    y,x,dest = dq.popleft()
    for ny,nx in [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]:
        if y-1<0 or R<=y+1 or x-1<0 or C<=x+1:
            continue
        elif c[ny][nx]=='#':
            continue
        elif ny==gy-1 and nx==gx-1:
            print(dest+1)
            exit()
        else:
            dq.append([ny,nx,dest+1])
            c[ny][nx]='#'

