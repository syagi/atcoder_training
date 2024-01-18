H,W=map(int,input().split())

dist=[]
for _ in range(10):
    dist.append(list(map(int,input().split())))

wall=[]
for _ in range(H):
    wall.append(list(map(int,input().split())))

N=10
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])

count=[0]*10
for i in range(H):
    for j in range(W):
        if wall[i][j]!=-1:
            count[wall[i][j]]+=1

ans=0
for i in range(10):
    ans += dist[i][1]*count[i]

print(ans)
