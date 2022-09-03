k=int(input())

mod=0

for i in range(1,k+1):
    mod=(mod*10+7)%k
    if mod==0:
        print(i)
        exit()

print(-1)