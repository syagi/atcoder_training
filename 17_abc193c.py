n=int(input())

num=0
for a in range(2,int(n**0.5)+1):
    for b in range(2,n):
        if(a**b>n):
            break
        else:
            num +=1

print(n-num)