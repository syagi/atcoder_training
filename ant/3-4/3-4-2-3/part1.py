N,M = map(int,input().split())
kuji = []
part3=True
inf = 1<<60
for m in range(M):
    C,cost = map(int,input().split())
    if C!=1:
        part3=False
    for c in range(C):
        idol, p = map(float,input().split())
        kuji.append((int(idol)-1,p/100.0,cost))

#print(kuji)
# 部分点1
if N==1 and M==1:
    ans=kuji[0][2]

# 部分点2
elif N==1:
    k = min(kuji,key=lambda x: x[2])
    ans=k[2]

# 部分点3
elif part3:
    ans=0
    for n in range(N):
        ks=list(filter(lambda x: x[0]==n,kuji))
        k=min(ks,key=lambda x: x[2])
        ans+=k[2]

# 部分点4
elif N<=2:
    ans=0
    for n in range(N):
        ks=list(filter(lambda x: x[0]==n,kuji))
        k=min(ks,key=lambda x: x[2]/x[1])
        ans+=k[2]/k[1]

# 部分点5
elif M==1:
    ans=0
    # dp[S] 今持ってるカードSからあと幾らかかるか
    dp= [inf] * (1<<N)
    dp[-1] = 0 # フルコンプ
#    for mask in range((1<<N)-1):
#        for i in range(N):



print(ans)