n,m,h,k = map(int,input().split())

s=[]
for _ in range(n):
    s.append(int(input()))

edge=[]
for _ in range(m):
    a,b = map(int,input().split())
    edge.append([a,b])

edge.sort(key=lambda x: x[1])

for i in range(m):
    x=edge[i][0]
    y=edge[i][1]
    # 上にたどる
    j=y-1
    while j>0:
        if edge[j][0]==x:
            

