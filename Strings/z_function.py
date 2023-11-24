def trivial(pos, arr, string):
    while pos + arr[pos] < len(string) and string[arr[pos]] == string[pos + arr[pos]]:
        arr[pos] += 1
    return


def z_func_triv(s: str) -> list:
    length = len(s)
    z = [0] * length
    for i in range(1, length):
        trivial(i, z, s)
    return z


def z_func(s: str) -> list:
    z, boundaries = [0] * len(s), [0, 0]

    def update(pos: int):
        if pos + z[pos] - 1 > boundaries[1]:
            boundaries[0], boundaries[1] = pos, pos + z[pos] - 1
        return

    for i in range(1, len(s)):
        if i <= boundaries[1]:
            z[i] = min(boundaries[1] - i + 1, z[i - boundaries[0]])
        trivial(i, z, s)
        update(i)
    return z
