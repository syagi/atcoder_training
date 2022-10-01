N=int(input())

if(N==1):
    print(input())
    exit()

t=[]
for i in range(N):
    t.append(int(input()))

t_min=50*4

for i in range(1<<N):
    t_1=0
    t_2=0
    for j in range(N):
        if(i & (1 << j) ):
            t_1+=t[j]
        else:
            t_2+=t[j]
    t_min=min(t_min,max(t_1,t_2))

print(t_min)
