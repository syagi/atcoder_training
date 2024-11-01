N=int(input())
L=list(map(int,input().split()))

length=[]
i=0
while i<N:
    i+=1
    cnt=1
    while i<N and L[i-1]!=L[i]:
        cnt+=1
        i+=1
    length.append(cnt)

for i in range(len(length)-2):
    length[i]+=length[i+1]+length[i+2]
    
ans=max(length)

print(ans)