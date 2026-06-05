import sys
from collections import deque


class Dinic:
    """二部グラフの最大マッチングを求めるための Dinic 法。

    今回は容量がすべて 1 のグラフだが、実装を素直な最大流として書いておく。
    頂点数は高々 2N + 2 <= 202 程度なので、十分高速。
    """

    def __init__(self, n: int) -> None:
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, fr: int, to: int, cap: int) -> None:
        """fr -> to に容量 cap の辺を追加する。"""

        forward = [to, cap, None]
        backward = [fr, 0, forward]
        forward[2] = backward

        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def bfs(self, source: int, sink: int) -> bool:
        """残余グラフ上で、source からの距離レベルを作る。"""

        self.level = [-1] * self.n
        self.level[source] = 0
        que = deque([source])

        while que:
            v = que.popleft()
            for to, cap, _ in self.graph[v]:
                if cap > 0 and self.level[to] == -1:
                    self.level[to] = self.level[v] + 1
                    que.append(to)

        return self.level[sink] != -1

    def dfs(self, v: int, sink: int, flow: int) -> int:
        """レベルグラフ上で、v から sink へ流せるだけ流す。"""

        if v == sink:
            return flow

        while self.it[v] < len(self.graph[v]):
            edge = self.graph[v][self.it[v]]
            to, cap, rev = edge

            if cap > 0 and self.level[v] < self.level[to]:
                pushed = self.dfs(to, sink, min(flow, cap))
                if pushed > 0:
                    edge[1] -= pushed
                    rev[1] += pushed
                    return pushed

            self.it[v] += 1

        return 0

    def max_flow(self, source: int, sink: int) -> int:
        """source から sink への最大流量を返す。"""

        flow = 0
        INF = 10**18

        while self.bfs(source, sink):
            self.it = [0] * self.n

            while True:
                pushed = self.dfs(source, sink, INF)
                if pushed == 0:
                    break
                flow += pushed

        return flow


def prime_table(n: int) -> bytearray:
    """0..n について、素数なら 1、そうでなければ 0 の表を作る。"""

    is_prime = bytearray(b"\x01") * (n + 1)

    if n >= 0:
        is_prime[0] = 0
    if n >= 1:
        is_prime[1] = 0

    p = 2
    while p * p <= n:
        if is_prime[p]:
            start = p * p
            step = p
            count = (n - start) // step + 1
            is_prime[start : n + 1 : step] = b"\x00" * count
        p += 1

    return is_prime


def main() -> None:
    input = sys.stdin.readline

    n = int(input())
    x = list(map(int, input().split()))

    # まずカードの表裏そのものではなく「状態が切り替わる境界」を見る。
    #
    # 例えばカード 4 だけが表なら、
    #   3 と 4 の間で 裏 -> 表
    #   4 と 5 の間で 表 -> 裏
    # となるので、境界点 4 と 5 を持つと考える。
    #
    # カード x が表であることは、境界 x と x+1 を 1 回ずつ反転することに対応する。
    # 隣接する表カードがある場合は、間の境界が 2 回出て消えるので xor で管理する。
    boundaries = set()
    for value in x:
        for boundary in (value, value + 1):
            if boundary in boundaries:
                boundaries.remove(boundary)
            else:
                boundaries.add(boundary)

    points = sorted(boundaries)

    # 長さ p の連続区間を反転すると、境界 l と l+p だけが反転する。
    # p は 3 以上の奇素数なので、1 回の操作で直接結べるのは
    # 「偶奇が違い、距離が素数」の 2 点。
    odd_points = [v for v in points if v % 2 == 1]
    even_points = [v for v in points if v % 2 == 0]

    max_distance = points[-1] - points[0] if points else 0
    is_prime = prime_table(max_distance)

    # 距離が奇素数の odd-even ペアを、1 回の操作で消せるペアとして最大数選ぶ。
    # これは二部グラフの最大マッチング。
    odd_count = len(odd_points)
    even_count = len(even_points)

    source = odd_count + even_count
    sink = source + 1
    dinic = Dinic(sink + 1)

    for i in range(odd_count):
        dinic.add_edge(source, i, 1)

    for j in range(even_count):
        dinic.add_edge(odd_count + j, sink, 1)

    for i, odd in enumerate(odd_points):
        for j, even in enumerate(even_points):
            distance = abs(odd - even)
            if is_prime[distance]:
                dinic.add_edge(i, odd_count + j, 1)

    one_operation_pairs = dinic.max_flow(source, sink)

    # 最大マッチングで取れたペアは 1 回で消せる。
    #
    # 残った同じ偶奇の境界 2 点は、2 回の操作で消せる。
    # 例: 距離が偶数 d の 2 点は、奇素数の差を使って 2 操作にできる。
    #
    # ただし、奇数側に 2 点・偶数側に 2 点だけ余るような場合は、
    # 同じ偶奇ペアをそれぞれ 2 回ずつ消すより、
    # 4 点まとめて 3 回で消せる。
    # そのため「同じ偶奇ペアの個数」が両方に 1 つずつ余ったら 3 回として数える。
    remaining_odd = odd_count - one_operation_pairs
    remaining_even = even_count - one_operation_pairs

    answer = one_operation_pairs
    answer += 2 * (remaining_odd // 2)
    answer += 2 * (remaining_even // 2)
    answer += 3 * (remaining_odd % 2)

    print(answer)


if __name__ == "__main__":
    main()
