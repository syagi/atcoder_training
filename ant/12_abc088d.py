H,W = map(int,input().split())

s=[ [] for _ in range(H)]

for i in range(H):
    s[i]=list(input())

white=0
black=0
for i in range(H):
    for j in range(W):
        if s[i][j]==".":
            white+=1
        else:
            black+=1

from collections import deque

dq = deque()
dq.append([0,0,0])
s[0][0]='#'

time=0
while dq:
    y,x,time = dq.popleft()
    for ny,nx in [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]:
        if ny<0 or H<=ny or nx<0 or W<=nx:
            continue
        elif s[ny][nx]=='#':
            continue
        elif ny==H-1 and nx==W-1:
            time+=1
            break
        else:
            dq.append([ny,nx,time+1])
            s[ny][nx]='#'
    else:
        continue
    break
else:
    print(-1)
    exit()

print(white-time-1)
