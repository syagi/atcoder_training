N,K = map(int,input().split())

S=[]
for _ in range(N):
    s=int(input())
    if s==0:
        print(N)
        exit(0)
    S.append(s)
    
ans=0
right = 0
pro=1
for left in range(N):
    while right<N and pro * S[right] <= K:
        pro *= S[right]
        right+=1
    ans=max(ans,right-left)
    
    if right==left:
        right+=1
    else:
        pro /= S[left]

print(ans)