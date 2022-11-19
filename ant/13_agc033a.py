H,W = map(int,input().split())

a=[ [] for _ in range(H)]

for i in range(H):
    a[i]=list(input())

from collections import deque

dq = deque()
white=0

for i in range(H):
    for j in range(W):
        if a[i][j]=='#':
            dq.append([i,j])
        else:
            white +=1

ans = 0
while white>0:
    dq_next=deque()
    while dq:
        y,x=dq.popleft()
        for ny,nx in [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]:
            if ny<0 or H<=ny or nx<0 or W<=nx :
                continue
            elif a[ny][nx]=='#':
                continue
            else:
                dq_next.append([ny,nx])
                a[ny][nx]='#'
                white -= 1
    else:
        ans += 1
        dq=dq_next

print(ans)