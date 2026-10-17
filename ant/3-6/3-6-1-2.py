import math

Tx,Ty = map(float,input().split())

N = int(input())
X=[]
Y=[]
for _ in range(N):
    x,y = map(float,input().split())
    X.append(x)
    Y.append(y)

def min_distance_to_edges(X, Y, Tx, Ty):
    N = len(X)
    ans = float("inf")

    for i in range(N):
        j = (i + 1) % N
        dx = X[j] - X[i]
        dy = Y[j] - Y[i]
        length_sq = dx * dx + dy * dy

        if length_sq == 0:
            # 両端が同じ座標の場合
            dist = math.hypot(Tx - X[i], Ty - Y[i])
        else:
            # Tから辺の直線に下ろした垂線の足の位置
            t = ((Tx - X[i]) * dx + (Ty - Y[i]) * dy) / length_sq

            # 垂線の足が線分の外なら、近い方の端点を使う
            t = max(0.0, min(1.0, t))
            px = X[i] + t * dx
            py = Y[i] + t * dy

            dist = math.hypot(Tx - px, Ty - py)

        ans = min(ans, dist)

    return ans

print(min_distance_to_edges(X,Y, Tx,Ty))