n=int(input())
s=list(input())
q=int(input())

r=False
for i in range(q):
    t,a,b = map(int,input().split())
    if(t==1):
        if(r):
            if(a<=n):
                a+=n
            else:
                a-=n
            if(b<=n):
                b+=n
            else:
                b-=n
            s[a-1],s[b-1]=s[b-1],s[a-1]
        else:
            s[a-1],s[b-1]=s[b-1],s[a-1]
    elif(r):
        r=False
    else:
        r=True
        
if(r):
    s=s[n:]+s[:n]

print(''.join(s))