X,Y = map(int,input().split())

a_i=X
ans=0

while(a_i<=Y):
    a_i*=2
    ans+=1

print(ans)