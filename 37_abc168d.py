n,m = map(int, input().split())

path=[[] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    path[a].append(b)
    path[b].append(a)

visited=[False]*(n+1)
visited[1]=True

from collections import deque

que = deque()
que.append(1)

ans=[0]*(n+1)

while 0<len(que):
    current=que.popleft()
    for dest in path[current]:
        if visited[dest]==False:
            visited[dest]=True
            ans[dest]=current
            que.append(dest)

print("Yes")
for i in range(2,n+1):
    print(ans[i])