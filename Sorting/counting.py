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


n = int(input())
length = int(input())
my_arr = [random.randint(0, n-1) for _ in range(length)]
print(my_arr)
series(my_arr, [simple])
