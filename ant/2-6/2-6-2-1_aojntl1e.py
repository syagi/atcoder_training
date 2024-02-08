
def extGCD(a,b):
    if (b==0):
        return (1,0)
    else:
        xd, yd = extGCD(b, a%b)
        return (yd, xd - a//b*yd)

a,b=map(int,input().split())

x,y=extGCD(a,b)
print(x,y)