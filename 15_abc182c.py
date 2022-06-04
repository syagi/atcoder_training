n=input()

a=0
b=0
s=0
for i in range(len(n)):
    s += int(n[i])
    c = int(n[i])%3
    if(c==1):
        a+=1
    if(c==2):
        b+=2

if(s%3==0):
    print(0)
if(s%3==1):
    if(a>0 and len(n)>1):
        print(1)
    elif(a>0 and len(n)==1):
        print(-1)
    elif(len(n)>2):
        print(2)
    else:
        print(-1) 
if(s%3==2):
    if(b>0 and len(n)>1):
        print(1)
    elif(b>0 and len(n)==1):
        print(-1)
    elif(len(n)>2):
        print(2)
    else:
        print(-1)