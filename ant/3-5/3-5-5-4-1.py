import sys
from heapq import heappush, heappop

input = sys.stdin.readline


class Edge:
    def __init__(self, to, rev, cap, cost):
        self.to = to          # 行き先ノード
        self.rev = rev        # 逆辺が、行き先ノードの隣接リストの何番目にあるか
        self.cap = cap        # 残り容量
        self.cost = cost      # 1 流量あたりのコスト


class MinCostFlow:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap, cost):
        """
        fr -> to に capacity=cap, cost=cost の辺を追加する。
        同時に、残余グラフ用の逆辺 to -> fr も追加する。
        """
        forward = Edge(to, len(self.g[to]), cap, cost)
        backward = Edge(fr, len(self.g[fr]), 0, -cost)

        self.g[fr].append(forward)
        self.g[to].append(backward)

    def flow(self, s, t, required_flow):
        """
        s から t へ required_flow だけ流すときの最小コストを返す。

        コストに負辺があるので、ポテンシャル h を使う。
        Dijkstra では reduced_cost = cost + h[v] - h[to] を使い、
        reduced_cost が非負になるように保つ。
        """
        n = self.n
        INF = 10**18

        result_cost = 0

        # h[v]:
        #   最短路計算を Dijkstra で行うためのポテンシャル。
        #
        # 今回は source -> 行 -> 列 に負辺がありうる。
        # 初期 h を全部 0 にすると reduced_cost が負になる可能性があるため、
        # 最初に Bellman-Ford 的に全辺緩和して初期ポテンシャルを作る。
        h = [INF] * n
        h[s] = 0

        for _ in range(n):
            updated = False
            for v in range(n):
                if h[v] == INF:
                    continue

                for e in self.g[v]:
                    if e.cap > 0 and h[e.to] > h[v] + e.cost:
                        h[e.to] = h[v] + e.cost
                        updated = True

            if not updated:
                break

        # required_flow が 0 になるまで、
        # 「現在の残余グラフでの最短路」に流せるだけ流す。
        while required_flow > 0:
            dist = [INF] * n
            prev_v = [-1] * n
            prev_e = [-1] * n

            dist[s] = 0
            pq = [(0, s)]

            while pq:
                d, v = heappop(pq)

                if dist[v] != d:
                    continue

                for i, e in enumerate(self.g[v]):
                    if e.cap == 0:
                        continue

                    # ポテンシャルで補正したコスト。
                    # h が適切なら、この値は非負になり、Dijkstra が使える。
                    nd = d + e.cost + h[v] - h[e.to]

                    if nd < dist[e.to]:
                        dist[e.to] = nd
                        prev_v[e.to] = v
                        prev_e[e.to] = i
                        heappush(pq, (nd, e.to))

            # この問題では必ず完全マッチングが存在するので、
            # t に到達できないことはない。
            if dist[t] == INF:
                raise RuntimeError("required flow cannot be sent")

            # ポテンシャルを更新する。
            # 次回以降も reduced_cost が非負になるようにする。
            for v in range(n):
                if dist[v] < INF:
                    h[v] += dist[v]

            # 今回見つかった最短路に流せる流量を調べる。
            # この問題では容量がすべて 1 なので、基本的には 1 になる。
            add_flow = required_flow
            v = t

            while v != s:
                pv = prev_v[v]
                pe = prev_e[v]
                add_flow = min(add_flow, self.g[pv][pe].cap)
                v = pv

            required_flow -= add_flow
            result_cost += add_flow * h[t]

            # 残余グラフを更新する。
            # 正方向の容量を減らし、逆方向の容量を増やす。
            v = t

            while v != s:
                pv = prev_v[v]
                pe = prev_e[v]

                e = self.g[pv][pe]
                e.cap -= add_flow
                self.g[v][e.rev].cap += add_flow

                v = pv

        return result_cost


def main():
    n = int(input())

    # W[i][j]: 空白マスに丸を書くコスト
    W = [list(map(int, input().split())) for _ in range(n)]

    # E[i][j]: 丸があるマスから丸を消すコスト
    E = [list(map(int, input().split())) for _ in range(n)]

    # F[i][j]: 初期状態。'o' なら丸あり、'.' なら空白
    F = [input().strip() for _ in range(n)]

    # ノード番号を決める。
    #
    # source = 0
    # 行ノード i = 1 + i
    # 列ノード j = 1 + n + j
    # sink = 1 + 2n
    source = 0
    row_start = 1
    col_start = 1 + n
    sink = 1 + 2 * n
    node_count = sink + 1

    mcf = MinCostFlow(node_count)

    # 「最初にすべての o を消した」と考えたときの基準コスト。
    # 実際に全部消すわけではなく、計算を楽にするための基準値。
    base_cost = 0

    # source -> 各行ノード
    # 各行から丸を置く列をちょうど 1 つ選びたいので、容量は 1。
    for i in range(n):
        mcf.add_edge(source, row_start + i, 1, 0)

    # 各列ノード -> sink
    # 各列にも丸はちょうど 1 つだけ置きたいので、容量は 1。
    for j in range(n):
        mcf.add_edge(col_start + j, sink, 1, 0)

    # 行ノード -> 列ノード
    #
    # この辺を 1 流すことが、
    # 「最終的にマス (i, j) に丸を置く」
    # という選択を表す。
    for i in range(n):
        for j in range(n):
            if F[i][j] == 'o':
                # いったん全部消す想定なので、消すコストを基準値に足す。
                base_cost += E[i][j]

                # しかしこのマスを最終的に丸ありとして選ぶなら、
                # 実際には消さなくてよい。
                # そのぶん E[i][j] だけ得するので、辺コストは -E[i][j]。
                cost = -E[i][j]
            else:
                # 空白マスを最終的に丸ありとして選ぶなら、
                # 新しく丸を書く必要がある。
                cost = W[i][j]

            mcf.add_edge(row_start + i, col_start + j, 1, cost)

    # n 個の丸を置く必要があるので、source から sink へ n 流す。
    # これにより、各行から 1 つ、各列へ 1 つの完全マッチングになる。
    additional_cost = mcf.flow(source, sink, n)

    # 実際の最小コストは、基準コスト + 選択による差分コスト。
    mincost = base_cost + additional_cost

    # 最小費用流の結果から、どの (行, 列) を選んだか復元する。
    selected = [[False] * n for _ in range(n)]

    for i in range(n):
        row_node = row_start + i

        for e in mcf.g[row_node]:
            # 行ノード -> 列ノード の辺だけを見る。
            if col_start <= e.to < col_start + n:
                j = e.to - col_start

                # 最初の容量は 1。
                # 流量 1 が流れた辺は、正方向の残り容量が 0 になっている。
                if e.cap == 0:
                    selected[i][j] = True

    # 選ばれた最終状態と初期状態を比べて、必要な操作を出力する。
    operations = []

    for i in range(n):
        for j in range(n):
            if F[i][j] == 'o' and not selected[i][j]:
                # 初期状態で丸があるが、最終状態では不要なので消す。
                operations.append((i + 1, j + 1, "erase"))

            elif F[i][j] == '.' and selected[i][j]:
                # 初期状態で空白だが、最終状態では丸が必要なので書く。
                operations.append((i + 1, j + 1, "write"))

    print(mincost)
    print(len(operations))

    for r, c, op in operations:
        print(r, c, op)


if __name__ == "__main__":
    main()