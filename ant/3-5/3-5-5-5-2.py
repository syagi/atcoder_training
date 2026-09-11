# AtCoder JAG2014Spring C - Decoding Ancient Messages
# 方針:
# 「選ぶ順番」は自由なので、ある完全マッチングで選んだ N 文字は
# 小さい順に並べて読むのが最も得になります。
#
# つまり、
#   各行から1つ、各列から1つ選ぶ
#   選ばれた文字の multiset を辞書順で最小にする
# という問題です。
#
# これは「小さい文字ほど圧倒的に価値が高い」重みを付けて、
# 最大重み完全マッチングを求めれば解けます。
#
# 例:
#   'A' の個数を最優先で最大化
#   それが同じなら 'B' の個数を最大化
#   ...
#
# 辞書順順なので、1つ1つの重みは大きくないと駄目
# Azz が BAA に負けないようにする
# base = N + 1 として、
#   A -> base^51
#   B -> base^50
#   ...
#   z -> base^0
# のように重みを付けると、1つ小さい文字の差は、
# 後ろの文字 N 個分より必ず大きくなります。

import sys


def hungarian_min(cost):
    """
    最小重み完全マッチングを求める Hungarian Algorithm。
    cost は 0-indexed の N x N 行列。

    戻り値:
        match_row[i] = 行 i に対応する列
    """
    n = len(cost)

    # 実装を楽にするため 1-indexed にする
    a = [[0] * (n + 1)]
    for row in cost:
        a.append([0] + row)

    # u, v はポテンシャル
    u = [0] * (n + 1)
    v = [0] * (n + 1)

    # p[j] = 列 j にマッチしている行
    p = [0] * (n + 1)

    # 経路復元用
    way = [0] * (n + 1)

    # 十分大きい値。
    # Python の int は多倍長なので巨大な重みでも安全。
    INF = 10**200

    for i in range(1, n + 1):
        # 行 i をマッチングに追加する
        p[0] = i
        j0 = 0

        minv = [INF] * (n + 1)
        used = [False] * (n + 1)

        while True:
            used[j0] = True
            i0 = p[j0]

            delta = INF
            j1 = 0

            # まだ使っていない列について、増加路を探す
            for j in range(1, n + 1):
                if used[j]:
                    continue

                # reduced cost
                cur = a[i0][j] - u[i0] - v[j]

                if cur < minv[j]:
                    minv[j] = cur
                    way[j] = j0

                if minv[j] < delta:
                    delta = minv[j]
                    j1 = j

            # ポテンシャルを更新する
            for j in range(0, n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta

            j0 = j1

            # 空いている列に到達したら増加路が見つかった
            if p[j0] == 0:
                break

        # 増加路に沿ってマッチングを張り替える
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break

    # match_row[row] = col に変換する
    match_row = [-1] * n
    for j in range(1, n + 1):
        row = p[j] - 1
        col = j - 1
        match_row[row] = col

    return match_row


def main():
    input = sys.stdin.readline

    N = int(input())
    grid = [input().strip() for _ in range(N)]

    # ASCII順: A-Z, a-z
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    # 文字ごとの順位
    rank = {ch: i for i, ch in enumerate(chars)}

    # 小さい文字ほど圧倒的に大きい価値を持たせる
    base = N + 1
    value = {}
    for ch in chars:
        r = rank[ch]
        value[ch] = pow(base, 51 - r)

    # Hungarian は「最小化」なので、最大化したい value にマイナスを付ける
    cost = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(-value[grid[i][j]])
        cost.append(row)

    # 最大価値になる完全マッチングを求める
    match = hungarian_min(cost)

    # 選んだ文字を集める
    selected = []
    for i in range(N):
        selected.append(grid[i][match[i]])

    # 選ぶ順番は自由なので、最も小さい文字列になるよう ASCII順に並べる
    selected.sort()

    print("".join(selected))


if __name__ == "__main__":
    main()