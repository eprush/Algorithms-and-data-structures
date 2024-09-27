n = int(input("How much numbers should we count? "))


def simple(arr: list, ascending=True) -> None:
    counts = [0] * n
    res = []
    for i in range(len(arr)):
        counts[arr[i]] += 1
    for i in range(n):
        for _ in range(counts[i]):
            res.append(i)
    for i in range(len(arr)):
        arr[i] = res[i]
    if not ascending:
        arr.reverse()
    return
