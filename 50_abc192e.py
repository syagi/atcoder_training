N,M,X,Y=map(int,input().split())

path=[[] for i in range(N+1)]

for i in range(M):
    a,b,t,k=map(int,input().split())
    path[a].append([b,t,k])
    path[b].append([a,t,k])

que=list()
MAX=10**20
import heapq
heapq.heappush(que,[0,X])
time=[MAX]*(N+1)
time[X]=0
confirmed=[False]*(N+1)

from math import ceil

while 0<len(que):
    c_time,c_place=heapq.heappop(que)
    if confirmed[c_place]:
        continue
    confirmed[c_place]=True
    for dest,t,k in path[c_place]:
        if not confirmed[dest]:
            dest_time=ceil(c_time/k)*k+t
            if dest_time<time[dest]:
                time[dest]=dest_time
                heapq.heappush(que,[dest_time,dest])

if time[Y]==MAX:
    print(-1)
else:
    print(time[Y])
