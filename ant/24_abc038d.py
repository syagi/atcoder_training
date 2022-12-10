N=int(input())

boxes=[]

for _ in range(N):
    w,h=map(int,input().split())
    boxes.append([w,h])

boxes.sort()
w_min=0
h_min=0
ans=0
for w,h in boxes:
    if w>w_min:
        if h>h_min:
            w_min=w
            h_min=h
            ans+=1
print(ans)

