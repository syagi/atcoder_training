D,G = map(int,input().split())

g=G/100
p=[]
c=[]
for i in range(D):
    p_i,c_i=map(int,input().split())
    p.append(p_i)
    c.append(c_i/100)

score=0
ans=0
for i in reversed(range(D)):
    score_i=p[i]*i+c[i]
    print(i,score,ans)
    if(score+score_i<g):
        score+=score_i
        ans+=p[i]
    elif(score+score_i==g):
        ans+=p[i]
        break
    else:
        for j in reversed(range(p[i])):
            score_j=j*i 
            print(j,score,ans)
            if(score+score_j<g):
                ans+=j+1
                break
        break

print(ans)
            


