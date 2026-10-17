def segments_intersect(A, B, P, Q):
    """線分ABとPQの交差を判定する。重なり・端点での接触はない前提。"""
    def cross(a, b, p):
        return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])

    # 各線分の両端が、もう一方の直線を挟む側にあるかを調べる。
    c1 = cross(A, B, P)
    c2 = cross(A, B, Q)
    c3 = cross(P, Q, A)
    c4 = cross(P, Q, B)
    return c1 * c2 < 0 and c3 * c4 < 0


Ax, Ay, Bx, By = map(float,input().split())
A=(Ax,Ay)
B=(Bx,By)

N=int(input())

X=[]
Y=[]
for _ in range(N):
    x,y = map(float,input().split())
    X.append(x)
    Y.append(y)

ans=0
for i in range(N):
    j = (i+1) % N
    P=(X[i],Y[i])
    Q=(X[j],Y[j])
    if segments_intersect(A,B,P,Q):
        ans+=1

print(ans//2+1)

