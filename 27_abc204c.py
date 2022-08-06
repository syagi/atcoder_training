n,m=map(int,input().split())

path=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    path[a].append(b)

from collections import deque

def BFS(start):
    visited=[False]*(n+1)
    
    visited[start]=True
    cnt=1
    que=deque()
    que.append(start)
    while 0<len(que):
        current_city=que.popleft()
        for dest_city in path[current_city]:
            if visited[dest_city]==False:
                visited[dest_city]=True
                cnt +=1
                que.append(dest_city)

    return cnt

ans = 0

for i in range(1,n+1):
    ans+=BFS(i)

print(ans)