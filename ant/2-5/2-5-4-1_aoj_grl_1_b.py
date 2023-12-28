V,E,src = map(int,input().split())

path=[]
for _ in range(E):
    s,t,d = map(int,input().split())
    path.append([s,t,d])
    # path.append([t,s,d])

# INF=10**10

def bellman_ford(src,V,path):
    dist = [float('inf')]*V
    dist[src] = 0
    for i in range(V):
        update = False
        for s,t,d in path:
            if dist[t] > dist[s]+d:
                dist[t]=dist[s]+d
                update=True
        if not update:
            break
        if i == V-1:
            # 負の閉路
            return -1
    return dist

ans = bellman_ford(src,V,path)
if ans==-1:
    print("NEGATIVE CYCLE")
else:
    for i in range(V):
        if ans[i]==float('inf'):
            print('INF')
        else:
            print(ans[i])

