import sys
from array import array


MOD = 1_000_000_007


def main() -> None:
    input = sys.stdin.readline
    X, S, N, K = map(int, input().split())

    # 全社の合計定員が人数より少ない場合、必ず誰かが就職できない。
    if S + N + K < X:
        print(0)
        return

    # fact[i]    = i!
    # invfact[i] = 1 / i!
    #
    # 最後に X! を掛ける形にしたいので、各カテゴリの人数 a に対して
    # invfact[a] を掛けながら和を取る。
    fact = [1] * (X + 1)
    for i in range(1, X + 1):
        fact[i] = fact[i - 1] * i % MOD

    invfact = [1] * (X + 1)
    invfact[X] = pow(fact[X], MOD - 2, MOD)
    for i in range(X, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD

    L = X + 1
    LL = L * L

    # 希望先の種類を以下の 7 種類に分ける。
    #
    #   x   : す社のみ
    #   y   : ぬ社のみ
    #   z   : け社のみ
    #   xy  : す社 or ぬ社
    #   yz  : ぬ社 or け社
    #   zx  : け社 or す社
    #   xyz : す社 or ぬ社 or け社
    #
    # ある人数の組が決まったとき、その表の数は
    #
    #   X! / (x! y! z! xy! yz! zx! xyz!)
    #
    # になる。
    #
    # そこで先に
    #
    #   sum 1 / (yz! zx! xyz!)
    #
    # を前計算しておく。
    #
    # pre[rem][cap_yz][cap_zx] =
    #   yz + zx + xyz = rem
    #   yz <= cap_yz
    #   zx <= cap_zx
    # を満たす全ての (yz, zx, xyz) についての
    #   invfact[yz] * invfact[zx] * invfact[xyz]
    # の和。
    pre = array("I", [0]) * (L * L * L)

    for rem in range(L):
        base = rem * LL

        # まず「ちょうど yz=a, zx=b」の値を入れる。
        # xyz は rem - a - b で自動的に決まる。
        for yz in range(rem + 1):
            row = base + yz * L
            for zx in range(rem - yz + 1):
                xyz = rem - yz - zx
                pre[row + zx] = invfact[yz] * invfact[zx] % MOD * invfact[xyz] % MOD

        # zx 方向の累積和。
        for yz in range(rem + 1):
            row = base + yz * L
            s = 0
            for zx in range(rem + 1):
                s += pre[row + zx]
                if s >= MOD:
                    s -= MOD
                pre[row + zx] = s

        # yz 方向の累積和。
        for zx in range(rem + 1):
            s = 0
            for yz in range(rem + 1):
                idx = base + yz * L + zx
                s += pre[idx]
                if s >= MOD:
                    s -= MOD
                pre[idx] = s

    ans = 0

    # Hall の定理より、割り当て可能であるための条件は以下。
    #
    #   x <= S, y <= N, z <= K
    #   x + y + xy <= S + N
    #   y + z + yz <= N + K
    #   z + x + zx <= K + S
    #   X <= S + N + K
    #
    # x, y, z, xy を全探索し、残りの yz,zx,xyz は pre でまとめて足す。
    for x in range(min(S, X) + 1):
        wx = invfact[x]

        for y in range(min(N, X - x) + 1):
            wxy_single = wx * invfact[y] % MOD

            for z in range(min(K, X - x - y) + 1):
                used = x + y + z

                # xy は x + y + xy <= S + N を満たす範囲だけ。
                max_xy = min(X - used, S + N - x - y)

                # 残り側の制約。
                # yz <= N + K - y - z
                # zx <= K + S - z - x
                cap_yz = N + K - y - z
                cap_zx = K + S - z - x

                base_weight = wxy_single * invfact[z] % MOD

                for xy in range(max_xy + 1):
                    rem = X - used - xy

                    cy = cap_yz if cap_yz < rem else rem
                    cz = cap_zx if cap_zx < rem else rem

                    weight = base_weight * invfact[xy] % MOD
                    weight = weight * pre[rem * LL + cy * L + cz] % MOD

                    ans += weight
                    if ans >= MOD:
                        ans -= MOD

    # ここまでの ans は
    #   sum 1 / (x! y! z! xy! yz! zx! xyz!)
    # なので、最後に X! を掛ける。
    print(ans * fact[X] % MOD)


if __name__ == "__main__":
    main()
