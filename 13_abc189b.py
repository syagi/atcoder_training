n, x = map(int,input().split())

a=0
for i in range(n):
    v,p=map(int,input().split())
    a+=v*p
    if(a>x*100):
        print(i+1)
        exit()
print(-1)
