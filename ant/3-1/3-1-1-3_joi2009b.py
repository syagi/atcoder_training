import bisect

d=int(input())
n=int(input())
m=int(input())

shop=[0]
for i in range(n-1):
    d_i=int(input())
    shop.append(d_i)
shop.append(d)

shop.sort()
# print(shop)
order=[]
for _ in range(m):
    k_i=int(input())
    order.append(k_i)

ans=0
for k in order:
    i=bisect.bisect_left(shop,k)
    # print(shop[i],k,shop[i+1])
    ans+= min(abs(shop[i-1]-k),abs(shop[i]-k))
print(ans)