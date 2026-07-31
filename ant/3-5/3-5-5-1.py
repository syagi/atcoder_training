import sys

sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline

    r, c = map(int, input().split())
    grid = [input().strip() for _ in range(r)]

    # 「広告を打てるマス」= '.' の個数
    # 最後にここから最大マッチング数を引く
    dot_count = 0

    # 二部グラフの左側に置く頂点だけに番号を振る
    # ここでは (i + j) % 2 == 0 の '.' マスを左側とする
    left_id = [[-1] * c for _ in range(r)]

    left_count = 0

    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                dot_count += 1

                if (i + j) % 2 == 0:
                    left_id[i][j] = left_count
                    left_count += 1

    # adj[v] := 左側頂点 v から到達できる右側のマス一覧
    #
    # 右側の頂点には番号を振らず、座標 (ni, nj) のまま扱う。
    # matching[ni][nj] に「その右側マスとマッチしている左側頂点番号」を入れる。
    adj = [[] for _ in range(left_count)]

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    for i in range(r):
        for j in range(c):
            # 左側の '.' マスだけから辺を張る
            if left_id[i][j] == -1:
                continue

            v = left_id[i][j]

            # 上下左右の '.' マスは必ず右側になる
            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if not (0 <= ni < r and 0 <= nj < c):
                    continue

                if grid[ni][nj] == '.':
                    adj[v].append((ni, nj))

    # matching[i][j] := 右側のマス (i, j) とマッチしている左側頂点
    # 未マッチなら -1
    matching = [[-1] * c for _ in range(r)]

    def dfs(v, seen):
        """
        左側頂点 v から増加路を探す。

        増加路とは、
        「今はマッチングされていない右側頂点」までたどり着く道、
        あるいは既存のマッチングをずらすことで
        新しく v をマッチングできる道のこと。
        """
        for ni, nj in adj[v]:
            # 同じ DFS 中に同じ右側頂点を何度も見ない
            if seen[ni][nj]:
                continue

            seen[ni][nj] = True

            # 右側マス (ni, nj) が未使用なら、v とマッチさせる
            if matching[ni][nj] == -1:
                matching[ni][nj] = v
                return True

            # すでに別の左側頂点 u とマッチしている場合、
            # u を別の右側頂点へ逃がせるなら、v がここを使える
            u = matching[ni][nj]
            if dfs(u, seen):
                matching[ni][nj] = v
                return True

        # v をマッチングに追加できなかった
        return False

    # 二部グラフの最大マッチングを求める
    max_matching = 0

    for v in range(left_count):
        seen = [[False] * c for _ in range(r)]

        if dfs(v, seen):
            max_matching += 1

    # 二部グラフでは、
    # 最大独立集合 = 頂点数 - 最大マッチング
    answer = dot_count - max_matching

    print(answer)


if __name__ == "__main__":
    main()