import itertools

N,M,R=map(int,input().split())

r=list(map(lambda x: int(x)-1,input().split()))
# print(r)

dist= [ [float('inf')]*N for _ in range(N)]
for i in range(N):
    dist[i][i]=0

for _ in range(M):
    a,b,c = map(int,input().split())
    dist[a-1][b-1]=c
    dist[b-1][a-1]=c

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])

# print(dist)

ans=float('inf')
for v in itertools.permutations(r,R):
    sum = 0
    for i in range(R-1):
        sum += dist[v[i]][v[i+1]]
    # print(v,sum,ans)
    ans = min(ans,sum)

print(ans)