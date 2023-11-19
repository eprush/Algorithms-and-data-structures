def prefix_func(s: str):
    pi = [0] * len(s)

    def find_cur(pos: int) -> int:
        def find_prev() -> int:
            p = pi[pos - 1]
            while p > 0 and s[pos] != s[p]:
                p = pi[p - 1]
            return p

        c = find_prev()
        if s[i] == s[c]:
            c += 1
        return c

    for i in range(1, len(s)):
        pi[i] = find_cur(i)
    return pi[-1]
