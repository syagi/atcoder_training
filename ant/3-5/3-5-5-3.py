from collections import deque
import sys


def main():
    input = sys.stdin.readline

    N, M = map(int, input().split())
    S = [input().strip() for _ in range(N)]

    total_w = 0
    total_b = 0

    # 白マスを左側、黒マスを右側の頂点として扱う。
    # この問題では制約により、チェスボード状に
    # 偶数マスは w または .、奇数マスは b または . になっている。
    white_id = {}
    black_id = {}

    for i in range(N):
        for j in range(M):
            if S[i][j] == "w":
                white_id[(i, j)] = total_w
                total_w += 1
            elif S[i][j] == "b":
                black_id[(i, j)] = total_b
                total_b += 1

    # 方法3:
    # 隣接する w-b の 2x1 または 1x2 ブロックを食べると 100 点。
    #
    # これは、
    #
    #   頂点: 残っているチョコのマス
    #   辺: 隣接していて、片方が w、片方が b の組
    #
    # と見ると、「同じマスを重複して使わず、辺を最大何本選べるか」
    # という問題になる。
    #
    # 同じマスは一度食べたらもう使えないので、
    # 選ぶ辺同士は頂点を共有してはいけない。
    # これはまさに最大マッチング。
    #
    # さらに w と b に分けると二部グラフになるので、
    # 最大二部マッチングで「方法3を最大何回使えるか」を求める。
    graph = [[] for _ in range(total_w)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for (i, j), w_id in white_id.items():
        for di, dj in dirs:
            ni, nj = i + di, j + dj

            if not (0 <= ni < N and 0 <= nj < M):
                continue

            if S[ni][nj] == "b":
                graph[w_id].append(black_id[(ni, nj)])

    # Hopcroft-Karp 法で最大二部マッチングを求める。
    W = total_w
    B = total_b

    pair_w = [-1] * W
    pair_b = [-1] * B
    dist = [-1] * W

    def bfs():
        # まだペアになっていない白マスから、
        # 増加路を探すための距離を作る。
        q = deque()
        found = False

        for w in range(W):
            if pair_w[w] == -1:
                dist[w] = 0
                q.append(w)
            else:
                dist[w] = -1

        while q:
            w = q.popleft()

            for b in graph[w]:
                next_w = pair_b[b]

                # 未使用の黒マスに到達できたので、
                # マッチングを増やせる可能性がある。
                if next_w == -1:
                    found = True
                # すでに他の白マスとペアになっている黒マスなら、
                # その相手の白マスへ進む。
                elif dist[next_w] == -1:
                    dist[next_w] = dist[w] + 1
                    q.append(next_w)

        return found

    def dfs(w):
        # BFS で作った距離に沿って増加路を探し、
        # 見つかればペアのつなぎ替えを行う。
        for b in graph[w]:
            next_w = pair_b[b]

            if next_w == -1 or (dist[next_w] == dist[w] + 1 and dfs(next_w)):
                pair_w[w] = b
                pair_b[b] = w
                return True

        # この白マスからは、今回は増加路を作れない。
        dist[w] = -1
        return False

    adjacent_pairs = 0

    while bfs():
        for w in range(W):
            if pair_w[w] == -1 and dfs(w):
                adjacent_pairs += 1

    # 方法3で使ったぶんだけ、白と黒が1個ずつ減る。
    remaining_w = total_w - adjacent_pairs
    remaining_b = total_b - adjacent_pairs

    # 方法2:
    # 残った白と黒を、位置に関係なく1個ずつ選んで同時に食べると10点。
    #
    # ここでは隣接条件がないので、最大で
    # min(残り白数, 残り黒数) 組作れる。
    normal_pairs = min(remaining_w, remaining_b)

    remaining_w -= normal_pairs
    remaining_b -= normal_pairs

    # 方法1:
    # 最後に余ったチョコは1個ずつ食べるしかない。
    # 1個あたり1点。
    single_pieces = remaining_w + remaining_b

    answer = adjacent_pairs * 100 + normal_pairs * 10 + single_pieces
    print(answer)


if __name__ == "__main__":
    main()