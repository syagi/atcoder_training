from collections import deque
import sys


def main():
    input = sys.stdin.readline

    M, N = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    B = [list(map(int, input().split())) for _ in range(M)]

    # まず「反転だけで直す」場合を考える。
    # A[i][j] != B[i][j] であるマスは、色を1回反転すれば直せる。
    # よって反転だけなら、コストは不一致マス数。
    mismatch = [[A[i][j] != B[i][j] for j in range(N)] for i in range(M)]
    base_cost = sum(mismatch[i][j] for i in range(M) for j in range(N))

    # ここから「交換すると得できるペア」を探す。
    #
    # 隣接する2つの不一致マスについて、
    #
    #   片方が 0 -> 1 にしたいマス
    #   もう片方が 1 -> 0 にしたいマス
    #
    # なら、その2マスを交換するだけで両方正しい色になる。
    #
    # 反転で直すなら2マス分でコスト2だが、
    # 交換ならコスト1なので、このペアを使うとコストが1だけ得になる。
    #
    # つまり、
    #
    #   不一致マス = グラフの頂点
    #   交換で両方解決できる隣接ペア = グラフの辺
    #
    # と考えると、「得できる交換を最大何回できるか」は
    # 「頂点を共有しない辺を最大何本選べるか」という問題になる。
    #
    # なぜ頂点を共有してはいけないかというと、
    # 1つのマスは1回の交換にしか使えないから。
    # あるマスを交換で直したあと、さらに別の交換にも使うことはできない。
    #
    # この「頂点を共有しない辺の集合」をマッチングと呼ぶ。
    #
    # さらに、グリッドの上下左右の隣接では、
    # (i + j) の偶奇が必ず反転する。
    # そのため、マスを偶数側・奇数側に分けると二部グラフになり、
    # 最大二部マッチングで解ける。

    left_id = {}
    right_id = {}
    left_cells = []

    # 不一致マスだけを、偶奇で左右のグループに分ける。
    for i in range(M):
        for j in range(N):
            if not mismatch[i][j]:
                continue

            if (i + j) % 2 == 0:
                left_id[(i, j)] = len(left_cells)
                left_cells.append((i, j))
            else:
                right_id[(i, j)] = len(right_id)

    # graph[v] には、左側頂点 v から交換可能な右側頂点の番号を入れる。
    graph = [[] for _ in range(len(left_cells))]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for v, (i, j) in enumerate(left_cells):
        for di, dj in dirs:
            ni, nj = i + di, j + dj

            if not (0 <= ni < M and 0 <= nj < N):
                continue
            if not mismatch[ni][nj]:
                continue

            # この2マスを交換したとき、両方が目標の色になるかを確認する。
            #
            # 交換後:
            #   (i, j) には A[ni][nj] が来る
            #   (ni, nj) には A[i][j] が来る
            #
            # それぞれ B[i][j], B[ni][nj] と一致すれば、
            # このペアは交換1回で両方解決できる。
            if A[ni][nj] == B[i][j] and A[i][j] == B[ni][nj]:
                graph[v].append(right_id[(ni, nj)])

    # Hopcroft-Karp 法で最大二部マッチングを求める。
    #
    # pair_left[v] = 左側頂点 v がマッチしている右側頂点
    # pair_right[u] = 右側頂点 u がマッチしている左側頂点
    #
    # -1 は、まだマッチしていないことを表す。
    L = len(left_cells)
    R = len(right_id)

    pair_left = [-1] * L
    pair_right = [-1] * R
    dist = [-1] * L

    def bfs():
        # まだマッチしていない左側頂点を始点として、
        # 増加路を探すための距離を作る。
        #
        # 増加路とは、今のマッチングを1つ増やせる道のこと。
        q = deque()
        found = False

        for v in range(L):
            if pair_left[v] == -1:
                dist[v] = 0
                q.append(v)
            else:
                dist[v] = -1

        while q:
            v = q.popleft()

            for u in graph[v]:
                next_left = pair_right[u]

                # 空いている右側頂点に到達できた。
                # つまり、増加路の終点候補が見つかった。
                if next_left == -1:
                    found = True
                # その右側頂点がすでに別の左側頂点とマッチしているなら、
                # そのマッチ相手の左側頂点へ進む。
                elif dist[next_left] == -1:
                    dist[next_left] = dist[v] + 1
                    q.append(next_left)

        return found

    def dfs(v):
        # BFS で作った距離に沿って、実際に増加路をたどる。
        #
        # 空いている右側頂点まで到達できれば、
        # 道に沿ってマッチングのつなぎ替えを行い、
        # マッチング数を1増やせる。
        for u in graph[v]:
            next_left = pair_right[u]

            if next_left == -1 or (
                dist[next_left] == dist[v] + 1 and dfs(next_left)
            ):
                pair_left[v] = u
                pair_right[u] = v
                return True

        # この左側頂点からは、今回は増加路を作れない。
        dist[v] = -1
        return False

    matching = 0

    while bfs():
        for v in range(L):
            if pair_left[v] == -1 and dfs(v):
                matching += 1

    # 反転だけなら base_cost。
    # 交換可能ペアを1組使うたびに、
    #   反転2回 = コスト2
    #   交換1回 = コスト1
    # となり、コストが1だけ小さくなる。
    #
    # 最大 matching 組だけ得できるので、答えは base_cost - matching。
    print(base_cost - matching)


if __name__ == "__main__":
    main()