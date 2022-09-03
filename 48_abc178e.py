N=int(input())

point=[]

for i in range(N):
    x,y = map(int,input().split())
    point.append([x,y])

pointx2=[]
pointy2=[]
for x,y in point:
    pointx2.append(x+y)
    pointy2.append(x-y)

xdist_max=abs(max(pointx2)-min(pointx2))
ydist_max=abs(max(pointy2)-min(pointy2))

print(max(xdist_max,ydist_max))