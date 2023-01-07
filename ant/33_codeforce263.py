N=int(input())
group=list(map(int,input().split()))

ans=0
while len(group)>0:
   print(group)
   g_min=min(group)
   ans+=sum(group)+g_min
   group.remove(g_min)

print(ans)