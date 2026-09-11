import sys
import heapq


class Edge:
    def __init__(self, to, rev, cap, cost, row=-1, col=-1):
        self.to = to
        self.rev = rev
        self.cap = cap
        self.cost = cost

        # 復元用。行->列の辺だけに入れる
        self.row = row
        self.col = col


def add_edge(graph, fr, to, cap, cost, row=-1, col=-1):
    forward = Edge(to, len(graph[to]), cap, cost, row, col)
    backward = Edge(fr, len(graph[fr]), 0, -cost)
    graph[fr].append(forward)
    graph[to].append(backward)


def min_cost_flow(graph, s, t, flow):
    n = len(graph)

    # ポテンシャル。負辺がある残余グラフでも Dijkstra できるようにする
    potential = [0] * n

    result = 0

    while flow > 0:
        dist = [None] * n
        prev_v = [-1] * n
        prev_e = [-1] * n

        dist[s] = 0
        pq = [(0, s)]

        while pq:
            d, v = heapq.heappop(pq)
            if dist[v] != d:
                continue

            for i, e in enumerate(graph[v]):
                if e.cap == 0:
                    continue

                # reduced cost
                nd = d + e.cost + potential[v] - potential[e.to]

                if dist[e.to] is None or nd < dist[e.to]:
                    dist[e.to] = nd
                    prev_v[e.to] = v
                    prev_e[e.to] = i
                    heapq.heappush(pq, (nd, e.to))

        # この問題では必ず N 流せる
        if dist[t] is None:
            raise RuntimeError("cannot send enough flow")

        for v in range(n):
            if dist[v] is not None:
                potential[v] += dist[v]

        # 容量は全部 1 なので、基本的に 1 ずつ流れる
        add = flow
        v = t
        while v != s:
            e = graph[prev_v[v]][prev_e[v]]
            add = min(add, e.cap)
            v = prev_v[v]

        flow -= add
        result += potential[t] * add

        # 残余グラフを更新
        v = t
        while v != s:
            e = graph[prev_v[v]][prev_e[v]]
            e.cap -= add
            graph[v][e.rev].cap += add
            v = prev_v[v]

    return result


def char_rank(c):
    # ASCII順: A-Z, a-z
    if "A" <= c <= "Z":
        return ord(c) - ord("A")
    return 26 + ord(c) - ord("a")


def main():
    input = sys.stdin.readline

    N = int(input())
    grid = [input().strip() for _ in range(N)]

    base = N + 1

    # 小さい文字ほど大きい価値。
    # A が base^51、z が base^0。
    value = {}
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        r = char_rank(c)
        value[c] = pow(base, 51 - r)

    # コストを非負にするための大きな定数
    M = pow(base, 52)

    source = 2 * N
    sink = 2 * N + 1
    graph = [[] for _ in range(2 * N + 2)]

    # source -> row
    for i in range(N):
        add_edge(graph, source, i, 1, 0)

    # col -> sink
    for j in range(N):
        add_edge(graph, N + j, sink, 1, 0)

    # row -> col
    for i in range(N):
        for j in range(N):
            c = grid[i][j]

            # 最小費用流なので「価値が大きいほどコストが小さい」にする
            cost = M - value[c]

            # 復元用に row, col も持たせる
            add_edge(graph, i, N + j, 1, cost, i, j)

    # N 個選ぶ
    min_cost_flow(graph, source, sink, N)

    selected = []

    # 使われた row -> col 辺を探す。
    # 元の容量 1 の辺が cap 0 になっていれば、そこに流量 1 が流れたということ。
    for i in range(N):
        for e in graph[i]:
            if e.row != -1 and e.cap == 0:
                selected.append(grid[e.row][e.col])

    # 選ぶ順番は自由なので、最後にソートしたものが答え
    selected.sort()
    print("".join(selected))


if __name__ == "__main__":
    main()