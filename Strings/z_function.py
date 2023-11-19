def z_func_triv(s: str) -> list:
    length = len(s)
    z = [0] * length
    for i in range(1, length):
        while i + z[i] < length and s[z[i]] == s[i + z[i]]:
            z[i] += 1
    return z


def z_func(s: str) -> list:
    length = len(s)
    z = [0] * length
    boundaries = [0, 0]

    def update(pos: int):
        if pos + z[pos] - 1 > boundaries[1]:
            boundaries[0], boundaries[1] = pos, pos + z[pos] - 1
        return

    for i in range(1, length):
        if i <= boundaries[1]:
            z[i] = min(boundaries[1] - i + 1, z[i - boundaries[0]])
        while i + z[i] < length and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        update(i)
    return z
