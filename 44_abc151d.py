h,w = map(int,input().split())

maze=[]

for i in range(h):
    maze.append(list(input()))

from cmath import exp
from collections import deque

def explore(s_row,s_col):
    step=[[-1] * w for i in range(h)]
    step[s_row][s_col]=0
    que=deque()

    que.append([s_row,s_col])

    max_step=0
    while 0<len(que):
        c_row,c_col=que.popleft()
        c_step=step[c_row][c_col]
        for x,y in [ [c_row-1,c_col],
                     [c_row+1,c_col],
                     [c_row,c_col-1],
                     [c_row,c_col+1] ]:
            if 0<=x<h and 0<=y<w:
                if maze[x][y]=="." and step[x][y]==-1:
                    step[x][y]=c_step+1
                    max_step=max(max_step,step[x][y])
                    que.append([x,y])
    return max_step

ans=0

for row in range(h):
    for col in range(w):
        if maze[row][col]==".":
            ans=max(ans,explore(row,col))

print(ans)