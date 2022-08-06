n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()

hands=[]
ans=0

for i in range(n):
    if t[i]=="r":
        if i<k:
            ans+=p
            hands.append("p")
        elif k<=i and hands[i-k]!="p":
            ans+=p
            hands.append("p")
        else:
            hands.append("x")
    elif t[i]=="s":
        if i<k:
            ans+=r
            hands.append("r")
        elif k<=i and hands[i-k]!="r":
            ans+=r
            hands.append("r")
        else:
            hands.append("x")
    elif t[i]=="p":
        if i<k:
            ans+=s
            hands.append("s")
        elif k<=i and hands[i-k]!="s":
            ans+=s
            hands.append("s")
        else:
            hands.append("x")

print(ans)