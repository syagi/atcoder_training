N1=int(input())
A=[(0,0)]
for i in range(N1):
    x,y = map(int,input().split())
    A.append((x,y))
A.append((1000,0))
N2=int(input())
B=[(0,1000)]
for i in range(N2):
    x,y = map(int,input().split())
    B.append((x,y))
B.append((1000,1000))

def point_segment_dist2(p, a, b):
    """点pと線分abの距離の2乗を返す。"""
    vx, vy = b[0] - a[0], b[1] - a[1]
    wx, wy = p[0] - a[0], p[1] - a[1]
    length2 = vx * vx + vy * vy

    # 両端が同じ座標なら、点同士の距離になる。
    if length2 == 0:
        return wx * wx + wy * wy

    t = (wx * vx + wy * vy) / length2
    t = max(0.0, min(1.0, t))
    dx, dy = wx - t * vx, wy - t * vy
    return dx * dx + dy * dy


segments_a = list(zip(A, A[1:]))
segments_b = list(zip(B, B[1:]))

answer2 = float("inf")
for a, b in segments_a:
    for c, d in segments_b:
        # 交差しない線分間の最短距離は、端点から相手の線分への距離の最小値。
        answer2 = min(
            answer2,
            point_segment_dist2(a, c, d),
            point_segment_dist2(b, c, d),
            point_segment_dist2(c, a, b),
            point_segment_dist2(d, a, b),
        )

print(f"{answer2 ** 0.5:.12f}")
