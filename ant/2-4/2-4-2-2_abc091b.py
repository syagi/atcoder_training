N=int(input())

s={}
for _ in range(N):
    si=input()
    if si in s:
        s[si]+=1
    else:
        s[si]=1

M=int(input())
t={}
for _ in range(M):
    ti=input()
    if ti in t:
        t[ti]+=1
    else:
        t[ti]=1

ans=0
for word in s.keys():
    if word in t:
        ans = max(ans, s[word]-t[word])
    else:
        ans = max(ans, s[word])

print(ans)