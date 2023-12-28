N,M = map(int,input().split())
INF=float('inf')
path=[]

for _ in range(M):
    a,b,c = map(int,input().split())
    path.append([a-1,b-1,c*-1])

def bellman_ford(src,V,path):
    dist = [INF]*V
    dist[src] = 0
    for i in range(V):
        update = False
        for s,t,d in path:
            if dist[s]!=INF and dist[t] > dist[s]+d:
                dist[t]=dist[s]+d
                update=True

    loop=[False]*N
    for i in range(N):
        for s,t,d in path:
            if  dist[t]>dist[s]+d :
                dist[t]=dist[s]+d
                loop[t]=True
            if loop[s]==True:
                loop[t]=True
    return dist,loop

ans,loop=bellman_ford(0,N,path)
if loop[N-1]:
    print("inf")
else:
    print(ans[N-1]*-1)