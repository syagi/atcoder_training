# https://ferin-tech.hatenablog.com/entry/2018/02/08/023409
import math
N,M,K=map(int,input().split())
N+=1
M+=1
ans=0

for i in range(N):
    for j in range(M):
        for k in range(N):
            for l in range(M):
                w = abs(k-i)
                h = abs(l-j)

                if(w==0):
                    if(h+1==K):
                        ans+=1
                    continue
                if(h==0):
                    if(w+1==K):
                        ans+=1
                    continue

                g=math.gcd(w,h)
                w /= g
                h /= g
                if((abs(k-i)/w+1)==K):
                    ans+=1

print(ans/2)