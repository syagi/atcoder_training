N=int(input())

reds=[]
blues=[]

for _ in range(N):
    x,y=map(int,input().split())
    reds.append((x,y))
for _ in range(N):
    x,y=map(int,input().split())
    blues.append((x,y))

blues.sort()

ans=0
for bluex,bluey in blues:
    # print(bluex,bluey)
    red_max=(-1,-1)
    for redx,redy in reds:
        if redx<bluex and redy<bluey and red_max[1]<redy:
            red_max=(redx,redy)
    if red_max!=(-1,-1):
        ans+=1
        # print(bluex,bluey,red_max[0],red_max[1])
        reds.remove(red_max)
    
print(ans)

