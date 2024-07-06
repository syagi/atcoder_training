N=int(input())

# cx+d=0
def solve(c,d):
    if d==0:
        return (0,0)
    elif d>0:
        return (1,0)
    else:
        return (0,1)

# bx^2+cx+d=0
def solve(b,c,d):
    if d==0:
        return solve(b,c)
    else:
        tmp = -c*c + 4*b*d
        if tmp>0:
            return (0,0)
        elif d<0:
            return (1,1)
        elif c>0:
            return (0,2)
        else:
            return (2,0)

# ax^3+bx^2+cx+d=0
# https://manabitimes.jp/math/1063
def solve(a,b,c,d):
    if a<0:
        return solve(-1*a,-1*b,-1*c,-1*d)
    elif d==0:
        return solve(b,c,d)
    else:
        tmp = -4*a*c^3 - 27*a^2*d^2 + b^2*c^2 + 18*a*b*c*d - 4*b^3*d
    


for _ in range(N):
    a,b,c,d = map(int,input().split())
    solve(a,b,c,d)