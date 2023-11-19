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
    left, right = 0, 0
    for i in range(1, length):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        while i + z[i] < length and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1
    return z
