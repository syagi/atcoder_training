import heapq
import sys


class MinCostFlow:
    """最小費用流を求めるクラス。

    残余グラフ上で「今いちばん安い s-t パス」を何度も選び、
    そのパスへ可能なだけ流す、という方針で解く。

    ただし、流した後には逆辺が現れ、その逆辺のコストは負になる。
    負の辺があると普通の Dijkstra は使えないので、
    ポテンシャル h[v] を使って辺の重みを非負に直してから Dijkstra する。
    """

    def __init__(self, n: int) -> None:
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, fr: int, to: int, cap: int, cost: int) -> None:
        """fr -> to に容量 cap、コスト cost の辺を追加する。

        最小費用流では「残余グラフ」を扱うため、辺を追加するときに
        逆向きの辺も同時に作っておく。

        forward:
            実際に入力で与えられた向きの辺。
            cap は「まだ追加で流せる量」を表す。

        backward:
            後から流量を取り消すための逆辺。
            例えば forward に 3 流した後なら、backward には 3 の容量ができる。
            取り消すと費用も戻るので、コストは -cost にする。
        """

        forward = [to, cap, cost, None]
        backward = [fr, 0, -cost, forward]
        forward[3] = backward

        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def min_cost_flow(self, source: int, sink: int, required_flow: int) -> int:
        """source から sink へ required_flow だけ流す最小費用を返す。

        流しきれない場合は -1 を返す。
        """

        n = self.n
        INF = 10**30

        # h[v] は頂点 v のポテンシャル。
        #
        # Dijkstra では、元のコスト cost(u, v) の代わりに
        #   cost(u, v) + h[u] - h[v]
        # という「 reduced cost 」を使う。
        #
        # 問題の入力コスト d_i はすべて 0 以上なので、最初は h=0 でよい。
        # 1 回 Dijkstra したあと、h[v] += dist[v] と更新すると、
        # 次回以降も到達可能な辺の reduced cost が非負に保たれる。
        potential = [0] * n

        total_cost = 0
        remaining_flow = required_flow

        while remaining_flow > 0:
            # dist[v]:
            #   reduced cost で見た source から v までの最短距離。
            #
            # prev_v[v], prev_e[v]:
            #   最短路木で v の直前にいた頂点と、使った辺。
            #   sink から source へ逆にたどることで、実際に流すパスを復元する。
            dist = [INF] * n
            prev_v = [-1] * n
            prev_e = [None] * n

            dist[source] = 0
            heap = [(0, source)]

            while heap:
                current_dist, v = heapq.heappop(heap)

                if dist[v] < current_dist:
                    continue

                for edge in self.graph[v]:
                    to, cap, cost, _ = edge

                    # 残り容量が 0 の辺には、これ以上流せない。
                    if cap == 0:
                        continue

                    # ポテンシャルで補正したコスト。
                    # これが非負なので Dijkstra が使える。
                    reduced_cost = cost + potential[v] - potential[to]
                    next_dist = current_dist + reduced_cost

                    if next_dist < dist[to]:
                        dist[to] = next_dist
                        prev_v[to] = v
                        prev_e[to] = edge
                        heapq.heappush(heap, (next_dist, to))

            # sink に到達できないなら、残りの流量はどうやっても流せない。
            if dist[sink] == INF:
                return -1

            # 次回の Dijkstra でも reduced cost が非負になるように、
            # 到達できた頂点のポテンシャルを更新する。
            #
            # dist が INF の頂点は今回 source から到達不能なので、更新しない。
            for v in range(n):
                if dist[v] < INF:
                    potential[v] += dist[v]

            # 見つかった最短路に、可能なだけまとめて流す。
            #
            # 1 ずつ流すと最大 F 回かかる。
            # パス上の最小残余容量ぶんだけ流せば、少なくともどれかの辺が詰まるため、
            # 無駄な反復を減らせる。
            add_flow = remaining_flow
            v = sink
            while v != source:
                edge = prev_e[v]
                add_flow = min(add_flow, edge[1])
                v = prev_v[v]

            remaining_flow -= add_flow

            # potential[sink] は、元のコストで見た source -> sink 最短路の費用になる。
            # そのパスへ add_flow だけ流すので、費用を add_flow 倍して足す。
            total_cost += add_flow * potential[sink]

            # 残余グラフを更新する。
            #
            # 使った forward 辺は残り容量が減る。
            # 対応する backward 辺は、後で取り消せる量が増える。
            v = sink
            while v != source:
                edge = prev_e[v]
                reverse_edge = edge[3]

                edge[1] -= add_flow
                reverse_edge[1] += add_flow

                v = prev_v[v]

        return total_cost


def main() -> None:
    input = sys.stdin.readline

    vertex_count, edge_count, flow = map(int, input().split())

    min_cost_flow = MinCostFlow(vertex_count)

    for _ in range(edge_count):
        fr, to, cap, cost = map(int, input().split())
        min_cost_flow.add_edge(fr, to, cap, cost)

    source = 0
    sink = vertex_count - 1

    answer = min_cost_flow.min_cost_flow(source, sink, flow)
    print(answer)


if __name__ == "__main__":
    main()
