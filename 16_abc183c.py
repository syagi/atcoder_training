import itertools

n,k=map(int,input().split())

t=[]
ans=0

for i in range(n):
    t.append(list(map(int,input().split())))

for trail in itertools.permutations(list(range(1,n))):
    time=0
    current=0
    for next in trail:
        time+=t[current][next]
        current=next
    time+=t[current][0]
    if time==k:
        ans+=1

print(ans)