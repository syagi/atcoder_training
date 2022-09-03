n,k = map(int,input().split())

A = [0] + list(map(int,input().split()))
visited=[-1]*(n+1)

visited[1]=0
ans=1
count=0
for i in range(k):
    count+=1
    ans=A[ans]
    if visited[ans]==-1:
        visited[ans]=count
    else:
        cycle=count-visited[ans]
        k-=count
        k%=cycle
        for i in range(k):
            ans=A[ans]
        break

print(ans)
