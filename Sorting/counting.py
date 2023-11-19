from Tests.sorting import series
import random


def simple(arr: list, ascending=True) -> None:
    counts = [0] * n
    res = []
    for i in range(length):
        counts[arr[i]] += 1
    for i in range(n):
        for _ in range(counts[i]):
            res.append(i)
    for i in range(length):
        arr[i] = res[i]
    if not ascending:
        arr.reverse()
    return
