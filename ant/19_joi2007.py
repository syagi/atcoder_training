x=1000-int(input())


ans=0
for c in [500, 100, 50, 10, 5, 1]:
    ans+=int(x/c)
    x%=c
print(ans)