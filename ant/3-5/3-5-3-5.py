import sys
from collections import deque


def is_good(value: int, a_limit: int, b_limit: int) -> bool:
    """操作できる条件を満たすか判定する。

    問題文の条件は
      |x| <= A
    または
      B <= |x| <= 2A
    のどちらか。
    """

    value = abs(value)
    return value <= a_limit or b_limit <= value <= 2 * a_limit


def hopcroft_karp(graph: list[list[int]], right_size: int) -> int:
    """二部グラフの最大マッチングを Hopcroft-Karp 法で求める。

    graph[left] は、左側頂点 left から接続できる右側頂点のリスト。
    戻り値はマッチング数。
    """

    left_size = len(graph)

    # pair_left[l]  = 左側 l のマッチ相手。なければ -1。
    # pair_right[r] = 右側 r のマッチ相手。なければ -1。
    pair_left = [-1] * left_size
    pair_right = [-1] * right_size

    # BFS で「未マッチ左頂点からの最短の増加パス」の層を作る。
    # DFS はこの層に沿ってだけ進むので、複数の増加パスをまとめて見つけられる。
    def bfs() -> bool:
        dist[:] = [-1] * left_size
        que = deque()

        for left in range(left_size):
            if pair_left[left] == -1:
                dist[left] = 0
                que.append(left)

        found_augmenting_path = False

        while que:
            left = que.popleft()

            for right in graph[left]:
                next_left = pair_right[right]

                # 未マッチの右頂点に到達できるなら、増加パス候補が存在する。
                if next_left == -1:
                    found_augmenting_path = True

                # 右頂点がすでにマッチしている場合は、
                # マッチング辺を逆向きにたどって次の左頂点へ進む。
                elif dist[next_left] == -1:
                    dist[next_left] = dist[left] + 1
                    que.append(next_left)

        return found_augmenting_path

    def dfs(left: int) -> bool:
        for right in graph[left]:
            next_left = pair_right[right]

            # 未マッチの右頂点に行ける、または層に沿ってさらに増加パスを伸ばせるなら採用。
            if next_left == -1 or (dist[next_left] == dist[left] + 1 and dfs(next_left)):
                pair_left[left] = right
                pair_right[right] = left
                return True

        # この左頂点からは今回の層グラフでは増加パスを作れない。
        # -1 にしておくと、同じ BFS フェーズ中の無駄な再探索を減らせる。
        dist[left] = -1
        return False

    matching = 0
    dist = [-1] * left_size

    while bfs():
        for left in range(left_size):
            if pair_left[left] == -1 and dfs(left):
                matching += 1

    return matching


def main() -> None:
    input = sys.stdin.readline

    n, a_limit, b_limit = map(int, input().split())

    answer = 0
    positives = []
    negatives = []

    for _ in range(n):
        a_i, b_i = map(int, input().split())
        diff = a_i - b_i

        # 単独で消せる要素は、必ず単独で消してよい。
        # ペアにしても操作回数は 1 回のままで、相手の要素を余分に消費してしまうため。
        if is_good(diff, a_limit, b_limit):
            answer += 1
            continue

        # ここに残る diff は単独では消せない。
        # |diff| は A より大きいので、同じ符号同士を足すと絶対値が 2A を超える。
        # したがって、ペアで消せる可能性があるのは正負の組だけ。
        if diff > 0:
            positives.append(diff)
        else:
            negatives.append(diff)

    # 正の diff と負の diff の組で、
    # |diff_i + diff_j| が条件を満たすものに辺を張る。
    graph = [[] for _ in range(len(positives))]

    for i, pos in enumerate(positives):
        for j, neg in enumerate(negatives):
            if is_good(pos + neg, a_limit, b_limit):
                graph[i].append(j)

    answer += hopcroft_karp(graph, len(negatives))
    print(answer)


if __name__ == "__main__":
    main()
