# AOJ 2316 人魚の魔女
#
# 解答方針：次に頂点が床へ接触する瞬間だけをシミュレーションする。
#
# 【円として考えるもの】
# 正方形そのものを円に置き換えるわけではない。
# 床に触れている頂点 P を固定して回すと、他の頂点の軌跡が円になる。
# 隣の頂点までの距離は1、対角の頂点までの距離は sqrt(2) なので、
# P を中心とする、この2種類の円と床の線分との交点を調べればよい。
# 正方形の中心の軌跡だけでは、どの頂点が先に接触するか分からない。
#
# 【折れ線で注意すること】
# 同じ直線上なら接地点が距離1ずつ進むが、折れ目では90度回る前に
# 先の斜面へ頂点が接触する。そのため、床に沿った距離の合計だけでは
# 色を決められない。鋭い谷では対角の頂点が先に接触することもある。
# 次の線分だけでなく、現在の支点より先の全線分を候補にする。
#
# 【接触候補の比較】
# 交点 Q までの距離ではなく、そこまでに必要な回転角を比較する。
# 隣の頂点の方向を基準とし、その現在の角度を alpha とすると、
# Q の偏角 theta に対して必要な時計回りの回転角は次のようになる。
#   隣の頂点：alpha - theta
#   対角の頂点：alpha + pi/4 - theta
# よって score = theta - offset と置けば、回転角は alpha - score。
# alpha は全候補で共通なので、score が最大の候補が最初に接触する。
# ここで offset は、隣の頂点なら0、対角の頂点なら pi/4 とする。
# 毎回 alpha や正方形の全頂点の座標を保存する必要はない。
#
# 【状態の更新と終了】
# 選んだ交点を新しい支点にして、載っている線分番号も更新する。
# 支点となる頂点の番号は、隣の頂点なら1、対角なら2進む。
# 色の状態は4周期なので、この進みの合計を4で割った余りで管理できる。
# これは90度回転した回数ではなく、頂点番号がいくつ進んだかである。
# 支点の x 座標が B を超えたら終了する。問題の保証により、この最後の
# 状態では辺が床に接地し、新しい支点がその辺の東端になる。
#
# 1回の更新で O(N) 個の線分を調べる。
# 接触による更新回数を K とすると、計算量は O(NK)、空間は O(N)。

import math
import sys


EPS = 1e-9
COLORS = ("Red", "Green", "Blue", "White")
# (支点からの距離の2乗, 角度の補正, 頂点番号の進み)
VERTICES = ((1.0, 0.0, 1), (2.0, math.pi / 4, 2))


def solve(data):
    it = iter(map(int, data.split()))
    n, start_x, goal_x = next(it), next(it), next(it)
    points = [(next(it), next(it)) for _ in range(n)]

    # 最初の接地辺の西端の x 座標が start_x。
    # そこから床に沿って距離1だけ進んだ東端を、最初の支点にする。
    x0, y0 = points[0]
    x1, y1 = points[1]
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy)
    px = start_x + dx / length
    py = y0 + (start_x - x0) * dy / dx + dy / length

    segment = 0  # 支点が載っている床の線分番号
    vertex_count = 0  # 支点となる頂点の進みを数える（実際の90度回転数ではない）

    while px <= goal_x:
        best_score = -math.inf
        best = None

        # 現在の支点より先にある床をすべて調べる。
        for i in range(segment, n - 1):
            ax, ay = (px, py) if i == segment else points[i]
            bx, by = points[i + 1]
            vx, vy = bx - ax, by - ay
            length2 = vx * vx + vy * vy
            if length2 < EPS * EPS:
                continue

            wx, wy = ax - px, ay - py
            dot = wx * vx + wy * vy

            for radius2, offset, advance in VERTICES:
                # Q = (ax, ay) + t * (vx, vy) とおき、
                # |Q - P|^2 = radius2 を t について解く。
                discriminant = dot * dot - length2 * (
                    wx * wx + wy * wy - radius2
                )
                if discriminant < -EPS:
                    continue

                root = math.sqrt(max(0.0, discriminant))
                for t in ((-dot - root) / length2, (-dot + root) / length2):
                    if not -EPS <= t <= 1.0 + EPS:
                        continue
                    t = max(0.0, min(1.0, t))
                    qx, qy = ax + t * vx, ay + t * vy
                    if qx <= px + EPS:
                        continue

                    # 対角の頂点は隣の頂点から45度ずれている。
                    # 基準をそろえると、角度の大きい候補ほど先に接触する。
                    score = math.atan2(qy - py, qx - px) - offset
                    if score > best_score:
                        best_score = score
                        best = (qx, qy, i, advance)

        if best is None:
            raise ValueError("次の接触点が見つかりません")

        px, py, segment, advance = best
        vertex_count += advance

    # 問題の保証により、目標を越える最後の状態では辺が接地している。
    return COLORS[vertex_count % 4]


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))
