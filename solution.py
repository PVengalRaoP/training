def Solve(N, P, A, B):
    MOD = 10**9 + 7
    L = min(N, P)

    def build(fixed, movable):
        freq = [0] * N
        for x in movable:
            freq[x % N] += 1

        bit = [0] * (N + 1)

        def add(idx, val):
            idx += 1
            while idx <= N:
                bit[idx] += val
                idx += idx & -idx

        def prefix(idx):
            idx += 1
            s = 0
            while idx:
                s += bit[idx]
                idx -= idx & -idx
            return s

        def kth(k):
            idx = 0
            step = 1 << (N.bit_length() - 1)
            while step:
                nxt = idx + step
                if nxt <= N and bit[nxt] < k:
                    idx = nxt
                    k -= bit[nxt]
                step >>= 1
            return idx

        for i in range(N):
            if freq[i]:
                add(i, freq[i])

        total = N
        C = []

        for i in range(L):
            x = fixed[i] % N
            target = (-x) % N
            before = prefix(target - 1) if target else 0
            if before < total:
                y = kth(before + 1)
            else:
                y = kth(1)

            C.append((x + y) % N)
            add(y, -1)
            total -= 1

        return C

    C1 = build(B, A)
    C2 = build(A, B)
    C = C1 if C1 < C2 else C2

    ans = 0
    power = 1
    for x in C:
        ans = (ans + x * power) % MOD
        power = (power * P) % MOD
    return ans
