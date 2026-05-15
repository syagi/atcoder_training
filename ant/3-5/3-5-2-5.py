import sys
from array import array


MOD = 1_000_000_007


def main() -> None:
    input = sys.stdin.readline
    X, S, N, K = map(int, input().split())

    # 3 社を合わせた定員が人数より少ないなら、どんな希望表でも全員は就職できない。
    if S + N + K < X:
        print(0)
        return

    # C[n][r] = nCr を MOD で割った値。
    # X <= 150 なので、パスカルの三角形で小さく作っておくと高速に参照できる。
    C = [[0] * (X + 1) for _ in range(X + 1)]
    for n in range(X + 1):
        C[n][0] = C[n][n] = 1
        for r in range(1, n):
            C[n][r] = (C[n - 1][r - 1] + C[n - 1][r]) % MOD

    # どの 2 社の合計定員も X 以上なら、Hall 条件のうち
    #   xs + xn + xsn <= S + N
    #   xs + xk + xsk <= S + K
    #   xn + xk + xnk <= N + K
    # は必ず満たされる。
    # その場合は「単独で 1 社だけを希望する人」が各社の定員を超えないことだけ見ればよい。
    # 7 種類の非空希望集合から自由に選ぶ総数 7^X から、
    # 単独希望者が定員超過する場合を包除原理で引く。
    if S + N >= X and S + K >= X and N + K >= X:
        caps = [S, N, K]

        def count_with_lower_bounds(lowers: list[int]) -> int:
            """指定された単独希望カテゴリが、それぞれ lower 以上になる表の数。"""
            selected = len(lowers)
            other_kinds = 7 - selected
            total = 0

            if selected == 0:
                return pow(7, X, MOD)

            if selected == 1:
                l0 = lowers[0]
                for c0 in range(l0, X + 1):
                    rest = X - c0
                    total += C[X][c0] * pow(other_kinds, rest, MOD)
                return total % MOD

            if selected == 2:
                l0, l1 = lowers
                for c0 in range(l0, X + 1):
                    choose0 = C[X][c0]
                    rem0 = X - c0
                    for c1 in range(l1, rem0 + 1):
                        rest = rem0 - c1
                        total += choose0 * C[rem0][c1] * pow(other_kinds, rest, MOD)
                return total % MOD

            l0, l1, l2 = lowers
            for c0 in range(l0, X + 1):
                choose0 = C[X][c0]
                rem0 = X - c0
                for c1 in range(l1, rem0 + 1):
                    choose01 = choose0 * C[rem0][c1] % MOD
                    rem1 = rem0 - c1
                    for c2 in range(l2, rem1 + 1):
                        rest = rem1 - c2
                        total += choose01 * C[rem1][c2] * pow(other_kinds, rest, MOD)
            return total % MOD

        ans = 0
        for mask in range(8):
            lowers = []
            bits = 0
            for i in range(3):
                if (mask >> i) & 1:
                    bits += 1
                    lowers.append(caps[i] + 1)

            add = count_with_lower_bounds(lowers)
            if bits % 2 == 0:
                ans += add
            else:
                ans -= add
            ans %= MOD

        print(ans)
        return

    L = X + 1
    LL = L * L

    # 人を希望先の種類で 7 分類する。
    #
    #   xs   : す社のみ
    #   xn   : ぬ社のみ
    #   xk   : け社のみ
    #   xsn  : す社 or ぬ社
    #   xsk  : す社 or け社
    #   xnk  : ぬ社 or け社
    #   xsnk : す社 or ぬ社 or け社
    #
    # Hall の定理より、全員を希望先に割り当てられる条件は以下で十分。
    #   xs <= S, xn <= N, xk <= K
    #   xs + xn + xsn <= S + N
    #   xs + xk + xsk <= S + K
    #   xn + xk + xnk <= N + K
    #   X <= S + N + K
    #
    # xs, xn, xk, xsn を固定すると、残り rem 人を
    # xsk, xnk, xsnk に分けるだけになる。
    # その「xsk が上限 A 以下、xnk が上限 B 以下」の場合の数を
    # dp[rem][A][B] として前計算しておく。
    #
    # array('I') は 32 bit 符号なし整数の配列。
    # Python の int の 3 次元リストよりかなり省メモリになる。
    # （およそ 125MB -> 14MB）
    dp = array("I", [0]) * (L * L * L)

    for rem in range(L):
        base = rem * LL

        # まずは「ちょうど xsk=a, xnk=b」の人数の選び方を入れる。
        # 残りは自動的に xsnk になる。
        for a in range(rem + 1):
            row = base + a * L
            choose_a = C[rem][a]
            rest = rem - a
            for b in range(rest + 1):
                dp[row + b] = choose_a * C[rest][b] % MOD

        # b 方向の累積和:
        # dp[rem][a][b] = sum_{j<=b} exact[a][j]
        for a in range(rem + 1):
            row = base + a * L
            run = 0
            for b in range(rem + 1):
                run += dp[row + b]
                if run >= MOD:
                    run -= MOD
                dp[row + b] = run

        # a 方向の累積和:
        # dp[rem][a][b] = sum_{i<=a, j<=b} exact[i][j]
        for b in range(rem + 1):
            run = 0
            for a in range(rem + 1):
                idx = base + a * L + b
                run += dp[idx]
                if run >= MOD:
                    run -= MOD
                dp[idx] = run

    ans = 0

    # xs, xn, xk, xsn を全探索する。
    # 合計人数が X を超える組は見ないので、最大でも C(X+4,4) 程度。
    for xs in range(S + 1):
        # xs 人を「す社のみ」にする人の選び方。
        choose_xs = C[X][xs]

        max_xn = min(N, X - xs)
        for xn in range(max_xn + 1):
            # さらに xn 人を「ぬ社のみ」にする。
            choose_xs_xn = choose_xs * C[X - xs][xn] % MOD

            max_xk = min(K, X - xs - xn)
            for xk in range(max_xk + 1):
                # さらに xk 人を「け社のみ」にする。
                after_three = X - xs - xn - xk
                base_ways = choose_xs_xn * C[X - xs - xn][xk] % MOD

                # xsn は「す社 or ぬ社」だけを希望する人。
                # Hall 条件 xs + xn + xsn <= S + N から上限が決まる。
                max_xsn = min(after_three, S + N - xs - xn)

                # 残りを xsk, xnk, xsnk に分けるときの上限。
                # xsk <= S + K - xs - xk
                # xnk <= N + K - xn - xk
                cap_xsk = S + K - xs - xk
                cap_xnk = N + K - xn - xk

                for xsn in range(max_xsn + 1):
                    rem = after_three - xsn

                    # after_three 人の中から xsn 人を選び、
                    # 残り rem 人の分け方は前計算 dp に任せる。
                    ways = base_ways * C[after_three][xsn] % MOD

                    a = cap_xsk if cap_xsk < rem else rem
                    b = cap_xnk if cap_xnk < rem else rem
                    ways = ways * dp[rem * LL + a * L + b] % MOD

                    ans += ways
                    if ans >= MOD:
                        ans -= MOD

    print(ans % MOD)


if __name__ == "__main__":
    main()
