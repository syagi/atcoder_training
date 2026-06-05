import sys
from collections import deque


def maximum_matching(graph: list[list[int]]) -> list[int]:
    """一般グラフの最大マッチングを Edmonds の Blossom アルゴリズムで求める。

    match[v] は頂点 v のマッチ相手を表す。マッチしていない場合は -1。

    この問題の N は 200 なので、O(N^3) 程度の素直な実装で十分間に合う。
    2 部グラフではないので、通常の Hopcroft-Karp ではなく Blossom が必要になる。
    """

    n = len(graph)
    match = [-1] * n

    def find_augmenting_path(root: int) -> bool:
        """root から始まる増加パスを 1 本探し、見つかれば match を更新する。"""

        # base[v]:
        #   Blossom として縮約された頂点集合の「代表」。
        #   縮約されていない通常時は base[v] == v。
        base = list(range(n))

        # parent[v]:
        #   交互木の中で、v に入ってきた直前の辺の相手。
        #   「未マッチ辺で parent[v] -> v に来た」と考える。
        parent = [-1] * n

        # used[v] が True の頂点は、交互木の偶数深さ側としてキューに入る。
        used = [False] * n
        used[root] = True
        que = deque([root])

        def lca(a: int, b: int) -> int:
            """交互木上で、a と b の Blossom の最小共通祖先を求める。"""

            seen = [False] * n

            while True:
                a = base[a]
                seen[a] = True
                if match[a] == -1:
                    break
                a = parent[match[a]]

            while True:
                b = base[b]
                if seen[b]:
                    return b
                b = parent[match[b]]

        def mark_blossom_path(v: int, blossom_base: int, child: int, in_blossom: list[bool]) -> None:
            """v から blossom_base までの道を Blossom として印を付ける。"""

            while base[v] != blossom_base:
                in_blossom[base[v]] = True
                in_blossom[base[match[v]]] = True

                # Blossom の内側でも交互木の親関係が復元できるようにしておく。
                parent[v] = child
                child = match[v]
                v = parent[match[v]]

        while que:
            v = que.popleft()

            for u in graph[v]:
                # 同じ Blossom の中の辺、または現在のマッチング辺は見ない。
                if base[v] == base[u] or match[v] == u:
                    continue

                # u が偶数深さ側にいるなら、v-u で奇サイクル（Blossom）ができる。
                if u == root or (match[u] != -1 and parent[match[u]] != -1):
                    blossom_base = lca(v, u)
                    in_blossom = [False] * n

                    mark_blossom_path(v, blossom_base, u, in_blossom)
                    mark_blossom_path(u, blossom_base, v, in_blossom)

                    # Blossom 全体を blossom_base に縮約する。
                    for x in range(n):
                        if in_blossom[base[x]]:
                            base[x] = blossom_base
                            if not used[x]:
                                used[x] = True
                                que.append(x)

                # u がまだ交互木に入っていないなら、v-u を未マッチ辺として木に加える。
                elif parent[u] == -1:
                    parent[u] = v

                    # 未マッチ頂点に到達したので、root から u までが増加パス。
                    if match[u] == -1:
                        cur = u
                        while cur != -1:
                            prev = parent[cur]
                            next_cur = match[prev] if prev != -1 else -1

                            match[cur] = prev
                            if prev != -1:
                                match[prev] = cur

                            cur = next_cur
                        return True

                    # u は奇数深さ側、match[u] は偶数深さ側として探索を続ける。
                    matched_vertex = match[u]
                    used[matched_vertex] = True
                    que.append(matched_vertex)

        return False

    # 未マッチ頂点を根にして、増加パスが見つかる限りマッチングを大きくする。
    for v in range(n):
        if match[v] == -1:
            find_augmenting_path(v)

    return match


def has_sunny_cycle(graph: list[list[int]], match: list[int], root: int) -> bool:
    """root を含む「よい奇サイクル」があるかを判定する。

    root 以外の頂点はすでに完全マッチングされているとする。

    Sunny Graph の条件は、
      1. root を含む奇サイクルを選ぶ
      2. その外側の頂点をマッチング辺だけで 2 頂点成分にする
    と言い換えられる。

    root を未マッチ頂点として Edmonds の交互木探索を行うと、
    root を含む Blossom（奇サイクル）が見つかった瞬間に条件を満たす。
    """

    n = len(graph)
    base = list(range(n))
    parent = [-1] * n
    used = [False] * n
    used[root] = True
    que = deque([root])

    def lca(a: int, b: int) -> int:
        """現在の交互木・縮約状態での最小共通祖先を求める。"""

        seen = [False] * n

        while True:
            a = base[a]
            seen[a] = True
            if match[a] == -1:
                break
            a = parent[match[a]]

        while True:
            b = base[b]
            if seen[b]:
                return b
            b = parent[match[b]]

    def mark_blossom_path(v: int, blossom_base: int, child: int, in_blossom: list[bool]) -> None:
        """Blossom 縮約のため、v から blossom_base までの道を印付けする。"""

        while base[v] != blossom_base:
            in_blossom[base[v]] = True
            in_blossom[base[match[v]]] = True

            parent[v] = child
            child = match[v]
            v = parent[match[v]]

    while que:
        v = que.popleft()

        for u in graph[v]:
            if base[v] == base[u] or match[v] == u:
                continue

            if u == root or (match[u] != -1 and parent[match[u]] != -1):
                blossom_base = lca(v, u)

                # 縮約される Blossom の代表が root なら、
                # root を含む奇サイクルが作れる。
                if blossom_base == root:
                    return True

                # root を含まない Blossom は縮約して、探索を続ける。
                # その内側の奇サイクルは答えそのものではないが、
                # 縮約することで外側の構造を正しく探索できる。
                in_blossom = [False] * n
                mark_blossom_path(v, blossom_base, u, in_blossom)
                mark_blossom_path(u, blossom_base, v, in_blossom)

                for x in range(n):
                    if in_blossom[base[x]]:
                        base[x] = blossom_base
                        if not used[x]:
                            used[x] = True
                            que.append(x)

            elif parent[u] == -1:
                parent[u] = v

                # root 以外は完全マッチング済みなので、未マッチ頂点には到達しないはず。
                # ただし実装を安全にしておくため、到達した場合は探索を打ち切らず無視する。
                if match[u] == -1:
                    continue

                used[match[u]] = True
                que.append(match[u])

    return False


def main() -> None:
    input = sys.stdin.readline

    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]
    graph_without_root = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1

        graph[a].append(b)
        graph[b].append(a)

        # まず「頂点 1 以外をすべてペアにできるか」を調べたい。
        # そのため、頂点 1 に接続する辺は除いたグラフも用意する。
        if a != 0 and b != 0:
            graph_without_root[a].append(b)
            graph_without_root[b].append(a)

    root = 0

    # Sunny なら、頂点 1 を含む奇サイクルの外側はもちろん完全マッチングできる。
    # さらに、奇サイクル上の頂点 1 以外もサイクル辺を 1 つおきに選べばペアにできる。
    # よって、まず「頂点 1 を除いた全頂点の完全マッチング」が必要条件になる。
    match = maximum_matching(graph_without_root)

    for v in range(1, n):
        if match[v] == -1:
            print("No")
            return

    # 頂点 1 以外を完全マッチングした状態から、
    # 頂点 1 を含む Blossom（奇サイクル）が見つかれば Sunny。
    if has_sunny_cycle(graph, match, root):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
