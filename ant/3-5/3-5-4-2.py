import heapq
import sys


class MinCostFlow:
    """最小費用流を求めるクラス。

    今回は「最大で limit 人(クラス)まで流し、これ以上流せなくなったら止める」
    という使い方をする。各増加路は、その時点で一番安い経路なので、
    到着できるクラス数を最大化しつつ、その人数での運賃合計を最小にできる。
    """

    def __init__(self, n: int) -> None:
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, fr: int, to: int, cap: int, cost: int) -> None:
        forward = [to, cap, cost, None]
        backward = [fr, 0, -cost, forward]
        forward[3] = backward

        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def min_cost_flow_up_to(self, source: int, sink: int, limit: int) -> tuple[int, int]:
        """source から sink へ最大 limit だけ流し、(流量, 最小費用)を返す。"""

        n = self.n
        INF = 10**30

        # コストは非負の列車辺と 0 の待機辺から始まるので初期 potential は 0 でよい。
        # 残余グラフに負辺が出ても、reduced cost を使えば Dijkstra できる。
        potential = [0] * n
        flow = 0
        cost_sum = 0

        while flow < limit:
            dist = [INF] * n
            prev_v = [-1] * n
            prev_e = [None] * n

            dist[source] = 0
            heap = [(0, source)]

            while heap:
                current_dist, v = heapq.heappop(heap)
                if current_dist != dist[v]:
                    continue

                for edge in self.graph[v]:
                    to, cap, cost, _ = edge
                    if cap == 0:
                        continue

                    reduced_cost = cost + potential[v] - potential[to]
                    next_dist = current_dist + reduced_cost
                    if next_dist < dist[to]:
                        dist[to] = next_dist
                        prev_v[to] = v
                        prev_e[to] = edge
                        heapq.heappush(heap, (next_dist, to))

            # もう s-t パスがなければ、それが到着可能な最大クラス数。
            if dist[sink] == INF:
                break

            for v in range(n):
                if dist[v] < INF:
                    potential[v] += dist[v]

            add_flow = limit - flow
            v = sink
            while v != source:
                edge = prev_e[v]
                add_flow = min(add_flow, edge[1])
                v = prev_v[v]

            flow += add_flow
            cost_sum += add_flow * potential[sink]

            v = sink
            while v != source:
                edge = prev_e[v]
                reverse_edge = edge[3]
                edge[1] -= add_flow
                reverse_edge[1] += add_flow
                v = prev_v[v]

        return flow, cost_sum


def solve_dataset(n: int, trains: list[list[tuple[int, int, int]]], class_count: int) -> tuple[int, int]:
    """1 データセットを時間展開グラフにして最小費用流で解く。

    元の問題では駅 1,2,...,n の順に移動するだけなので、
    「駅 i の時刻 t にいる」という状態を頂点にすればよい。

    辺の意味:
      1. 待機辺
         同じ駅で、時刻 t_k から次の時刻 t_{k+1} へ進む辺。
         容量は十分大きく、費用は 0。
         これにより「早く着いたクラスは後の列車まで待てる」ことを表す。

      2. 列車辺
         駅 i の出発時刻 x から、駅 i+1 の到着時刻 y へ進む辺。
         費用は運賃 c。
         容量を 1 にするだけだと「同じ到着時刻の別列車」が複数使えてしまう。

      3. 到着ゲート
         駅 i(2 以上)の各到着時刻 y について、容量 1 のゲートを置く。
         すべての列車辺はいったんゲートへ入り、ゲートから時刻ノードへ出る。
         これで「同じ駅に同時に到着するクラスは高々 1 つ」を表せる。

    同じ駅に滞在するクラスが複数いてもよいので、待機辺は容量無限にする。
    制限されるのは「到着イベント」だけ、というのがこの帰着のポイント。
    """

    INF_CAP = class_count

    # 1 クラスも到着できないことだけを事前判定するなら、
    # 「各駅に到着できる最早時刻」を前から更新する軽い DP でも分かる。
    # ただしこの問題の制約ではグラフも流量も小さいので、
    # ここでは特別扱いせず、最小費用流で s-t パスが 1 本も見つからない場合に
    # 自然に (0, 0) が返る形にしている。

    # times[i]: 駅 i で状態として必要な時刻。
    # 駅 i の出発時刻と到着時刻の両方を入れておくと、
    # 到着後に待機辺を通って、乗れる出発時刻へ自然に進める。
    times: list[list[int]] = [[] for _ in range(n)]
    arrival_times: list[set[int]] = [set() for _ in range(n)]

    for station in range(n - 1):
        for depart, arrive, _ in trains[station]:
            times[station].append(depart)
            times[station + 1].append(arrive)
            arrival_times[station + 1].add(arrive)

    for station in range(n):
        times[station] = sorted(set(times[station]))

    # 各「駅・時刻」ノードの番号を振る。
    time_node: list[dict[int, int]] = [dict() for _ in range(n)]
    node_count = 2  # 0: source, 1: sink
    source = 0
    sink = 1

    for station in range(n):
        for t in times[station]:
            time_node[station][t] = node_count
            node_count += 1

    # 到着ゲートのノード番号を振る。
    arrival_gate: list[dict[int, int]] = [dict() for _ in range(n)]
    for station in range(1, n):
        for t in arrival_times[station]:
            arrival_gate[station][t] = node_count
            node_count += 1

    mcf = MinCostFlow(node_count)

    # 駅 1 には全クラスが最初からいる。
    # 最初の時刻へ流して待機辺で後の出発へ進ませれば、任意の列車を選べる。
    if times[0]:
        mcf.add_edge(source, time_node[0][times[0][0]], INF_CAP, 0)

    # 各駅内で時間が進む待機辺。
    for station in range(n):
        for earlier, later in zip(times[station], times[station][1:]):
            mcf.add_edge(time_node[station][earlier], time_node[station][later], INF_CAP, 0)

    # 到着ゲート。駅 2 以降の同一到着時刻に入れる流量を 1 にする。
    for station in range(1, n):
        for t in arrival_times[station]:
            mcf.add_edge(arrival_gate[station][t], time_node[station][t], 1, 0)

    # 列車辺。列車そのものも、同じ列車に複数クラスが乗ると同時到着になるため容量 1。
    for station in range(n - 1):
        for depart, arrive, fare in trains[station]:
            mcf.add_edge(
                time_node[station][depart],
                arrival_gate[station + 1][arrive],
                1,
                fare,
            )

    # 目的地 n では、どの到着時刻でも sink へ出られる。
    for t in times[n - 1]:
        mcf.add_edge(time_node[n - 1][t], sink, INF_CAP, 0)

    return mcf.min_cost_flow_up_to(source, sink, class_count)


def main() -> None:
    input = sys.stdin.readline
    answers = []

    while True:
        line = input()
        if not line:
            break

        n = int(line)
        if n == 0:
            break

        trains: list[list[tuple[int, int, int]]] = []
        for _ in range(n - 1):
            m = int(input())
            section = [tuple(map(int, input().split())) for _ in range(m)]
            trains.append(section)

        class_count = int(input())
        flow, cost = solve_dataset(n, trains, class_count)
        answers.append(f"{flow} {cost}")

    print("\n".join(answers))


if __name__ == "__main__":
    main()
