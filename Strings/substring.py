from prefix import prefix_func
from z_function import z_func
special_symbol = "#"


# Knuth-Morris-Pratt algorithm
def search_KMP(text: str, substring: str) -> list:
    s = substring + special_symbol + text
    entrances, length = [], len(substring)
    for i in range(length + 1, len(s)):
        if prefix_func(s[:i]) == length:
            entrances.append(i - 2 * length - 1)
    return entrances


def search_z(text: str, substring: str) -> list:
    entrances, length = [], len(substring)
    s = substring + special_symbol + text
    z = z_func(s)
    for i in range(len(text)):
        if z[i + length + 1] == length:
            entrances.append(i)
    return entrances
