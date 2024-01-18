import math

def dfs(i):
    print(i)
    print(bars[i])
    if (bars[i][2]!=-1):
        red = dfs(bars[i][2])
    else:
        red = -1
    if (bars[i][3]!=-1):
        blue = dfs(bars[i][3])
    else:
        blue = -1

    if(red==-1 and blue==-1):
        gcd = math.gcd(bars[i][0],bars[i][1])
        red = int(bars[i][1]/gcd)
        blue = int(bars[i][0]/gcd)
    elif(red==-1):
        red = int(bars[i][0]*blue/bars[i][1])
    elif(blue==-1):
        blue = int(bars[i][1]*red/bars[i][0])

    print("i",i,"red:",red,"blue:",blue)
    return red+blue

for _ in range(15):
    n = int(input())
    if (n==0):
        exit(0)
    bars = []
    check = set(range(n))
    for _ in range(n):
        p,q,r,b = map(int,input().split())
        r-=1
        if(r!=-1):
            check.remove(r)
        b-=1
        if(b!=-1):
            check.remove(b)
        bars.append([p,q,r,b])
    ans = dfs(check.pop())
    print(ans)
