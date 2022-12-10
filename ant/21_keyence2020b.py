N=int(input())

robots=[]
for _ in range(N):
    x,l = map(int,input().split())
    robots.append([x-l,x+l])

robots.sort(key= lambda x:x[1])

tmp=robots[0][0]-1
ans=0

for l,r in robots:
    if(tmp<=l):
        tmp=r
        ans+=1

print(ans)