n,k = map(int,input().split())
p = list(map(int,input().split()))

p_ex = []

for i in range(n):
    p_ex.append((p[i]+1)/2)

p_ex_sum = []
p_ex_sum.append(p_ex[0])
for i in range(1,n):
    p_ex_sum.append(p_ex_sum[i-1]+p_ex[i])

ans=-1.0

for i in range(n-k+1):
    if i==0:
        ans=max(ans,p_ex_sum[k-1])
    else:
        ans=max(ans,p_ex_sum[i+k-1]-p_ex_sum[i-1])

print(ans)