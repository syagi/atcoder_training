import sys

input = sys.stdin.readline


def hungarian(cost):
    """
    最小費用割当問題を解くハンガリアン法。
     https://yukashun.com/hungarian_algorithm/

    cost[i][j]:
        i 行目に対応する丸を j 列目に置くときの「追加コスト」
        0-indexed の n x n 行列

    戻り値:
        assignment[i] = i 行目で選ぶ列 j
    """
    n = len(cost)

    # 以下の実装は 1-indexed で書くと分かりやすいので、
    # u, v, p, way はサイズ n+1 にしている。
    #
    # u[i], v[j]:
    #   行側・列側のポテンシャル
    #
    # p[j]:
    #   現在、列 j に割り当てられている行
    #
    # way[j]:
    #   増加路を復元するための情報
    u = [0] * (n + 1)
    v = [0] * (n + 1)
    p = [0] * (n + 1)
    way = [0] * (n + 1)

    # 1 行ずつ割当を増やしていく
    for i in range(1, n + 1):
        # 0 番列をダミーとして使い、そこに新しい行 i を仮に繋ぐ
        p[0] = i
        j0 = 0

        # minv[j]:
        #   今見ている増加路から列 j に到達するための最小の余裕
        minv = [10**18] * (n + 1)

        # used[j]:
        #   列 j がすでに探索済みかどうか
        used = [False] * (n + 1)

        while True:
            used[j0] = True

            # 現在の列 j0 に割り当てられている行 i0 を見る
            i0 = p[j0]

            # delta:
            #   次にポテンシャルをどれだけ更新するか
            delta = 10**18
            j1 = 0

            # 未使用の列について、余裕を更新する
            for j in range(1, n + 1):
                if used[j]:
                    continue

                # reduced cost
                cur = cost[i0 - 1][j - 1] - u[i0] - v[j]

                if cur < minv[j]:
                    minv[j] = cur
                    way[j] = j0

                if minv[j] < delta:
                    delta = minv[j]
                    j1 = j

            # ポテンシャルを更新する
            # これにより、少なくとも1つ新しい列へ進めるようになる
            for j in range(0, n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta

            j0 = j1

            # 空いている列に到達できたら増加路が見つかった
            if p[j0] == 0:
                break

        # 増加路を逆にたどって、割当を更新する
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break

    # p[j] = 行 なので、行 -> 列 の形に直す
    assignment = [-1] * n
    for j in range(1, n + 1):
        if p[j] != 0:
            assignment[p[j] - 1] = j - 1

    return assignment


def main():
    n = int(input())

    # W[i][j]: 空白のマスに丸を書くコスト
    W = [list(map(int, input().split())) for _ in range(n)]

    # E[i][j]: 丸があるマスから丸を消すコスト
    E = [list(map(int, input().split())) for _ in range(n)]

    # 初期状態
    F = [input().strip() for _ in range(n)]

    # まず「最初に存在する丸をすべて消す」と考える。
    # その費用を base_cost とする。
    #
    # その後、最終的に丸を残す/書く場所を各行各列1つずつ選ぶ。
    base_cost = 0
    cost = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if F[i][j] == 'o':
                # 最初に全部消す想定なので、消去コストを足しておく
                base_cost += E[i][j]

                # もしこのマスを最終的に丸ありにするなら、
                # 実際には消さなくてよい。
                # つまり E[i][j] だけ得をするので追加コストは -E[i][j]
                cost[i][j] = -E[i][j]
            else:
                # 空白マスを最終的に丸ありにするなら、
                # 新しく書く必要がある
                cost[i][j] = W[i][j]

    # 各行・各列から1つずつ選ぶ最小コストの配置を求める
    assignment = hungarian(cost)

    # 最終的に丸を置くマスを記録する
    selected = [[False] * n for _ in range(n)]
    add_cost = 0

    for i, j in enumerate(assignment):
        selected[i][j] = True
        add_cost += cost[i][j]

    mincost = base_cost + add_cost

    operations = []

    for i in range(n):
        for j in range(n):
            if F[i][j] == 'o' and not selected[i][j]:
                # 初期状態で丸があるが、最終状態では不要なので消す
                operations.append((i + 1, j + 1, "erase"))
            elif F[i][j] == '.' and selected[i][j]:
                # 初期状態で空白だが、最終状態では丸が必要なので書く
                operations.append((i + 1, j + 1, "write"))

    print(mincost)
    print(len(operations))

    for r, c, op in operations:
        print(r, c, op)


if __name__ == "__main__":
    main()