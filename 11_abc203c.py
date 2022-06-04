n,k = map(int,input().split())

friends={}
ans=0
for i in range(n):
    ai,bi=map(int,input().split())
    if(ai in friends):
        friends[ai]+=bi
    else:
        friends[ai]=bi

sorted_friends = sorted(friends.items(), key=lambda x:x[0])

for a,b in sorted_friends:
    if(ans+k<a):
        print(ans+k)
        exit()
    ans += a
    k = k - a + b
    if(k==0):
        print(ans)
        exit()

print(ans+k)
