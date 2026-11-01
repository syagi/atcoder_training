import math


def catch_time(dx, dy, speed, px, py, vx, vy):
    """犬が単独で追った場合の最短取得時刻。取得できなければ inf。"""
    # 犬の現在位置を D=(dx, dy)、速さを s=speed、
    # フリスビーの発射位置を P=(px, py)、速度を V=(vx, vy) とする。
    # t 秒後のフリスビーの位置（合流点）は Q(t)=P+tV。
    # 犬が t 秒以内にそこへ到達できる条件は、距離が走れる距離以下、つまり
    #   |P+tV-D| <= s*t
    # となる。初期位置が異なる場合、最初に到達できる瞬間には等号が成立する。
    # R=P-D=(rx, ry) と置き、両辺を二乗して展開すると、
    #   |R+tV|^2 = s^2*t^2
    #   (V・V-s^2)*t^2 + 2*(R・V)*t + R・R = 0
    # よって、下記の係数で a*t^2+b*t+c=0 を解けばよい。
    # 非負の実数解のうち最小のものが最短取得時刻で、なければ取得できない。
    # 取得時刻 t が決まれば、合流点は (px+vx*t, py+vy*t) で求まる。
    rx, ry = px - dx, py - dy
    a = vx * vx + vy * vy - speed * speed
    b = 2 * (rx * vx + ry * vy)
    c = rx * rx + ry * ry

    if c == 0:
        return 0.0

    # フリスビーと犬の速さが等しい場合は一次方程式になる。
    if a == 0:
        return -c / b if b < 0 else math.inf

    discriminant = b * b - 4 * a * c
    # 接する場合に、丸め誤差で判別式がわずかに負になるのを補正する。
    tolerance = 8 * math.ulp(b * b + abs(4 * a * c))
    if discriminant < -tolerance:
        return math.inf
    root = math.sqrt(max(0.0, discriminant))

    # 解の公式で近い数同士を引くことによる桁落ちを避ける。
    # 片方の解を q/a、もう片方を解の積 c/a から c/q として求める。
    q = -0.5 * (b + math.copysign(root, b))
    if q == 0:
        return math.inf
    times = [t for t in (q / a, c / q) if t >= 0]
    return min(times, default=math.inf)


while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    # D: 犬。(位置x, 位置y, 速度, 取得数)
    D = []
    for _ in range(N):
        x, y, v = map(float, input().split())
        D.append((x, y, v, 0))

    # F: フリスビー。(位置x, 位置y, 速度x, 速度y)
    F = []
    for _ in range(M):
        x, y, vx, vy = map(float, input().split())
        F.append((x, y, vx, vy))

    for px, py, vx, vy in F:
        times = [catch_time(x, y, v, px, py, vx, vy)
                 for x, y, v, count in D]
        winner = min(range(N), key=lambda i: times[i])
        elapsed = times[winner]

        for i in range(N):
            x, y, v, count = D[i]
            t = times[i]
            if i == winner:
                # 取得した犬は、取得時刻のフリスビーの位置にいる。
                x, y = px + vx * elapsed, py + vy * elapsed
                count += 1
            elif math.isfinite(t):
                # 自分の取得予定地点へ向けて、elapsed 秒だけ移動する。
                target_x, target_y = px + vx * t, py + vy * t
                x += (target_x - x) * (elapsed / t)
                y += (target_y - y) * (elapsed / t)
            # 取得できない犬は、その場で待機する。
            D[i] = (x, y, v, count)

    print(*(count for x, y, v, count in D))

