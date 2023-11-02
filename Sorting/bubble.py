from sort import experiment


def simple(arr: list, ascending=True) -> None:
    for _ in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    if not ascending:
        arr.reverse()
    return


def optimized(arr, ascending=True):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    if not ascending:
        arr.reverse()
    return


def best(arr, ascending=True):
    # if internal loop hasn't swapping,
    # there is a time to stop
    i = 0
    swapping = True
    while swapping:
        swapping = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapping = True
        i += 1

    if not ascending:
        arr.reverse()
    return


example = [-1, 1, 0, 1, 2, -10, -2, 0, 10]
print("The lenght of example array equals", len(example))
a = example.copy()

experiment(a, simple)
a = example.copy()

experiment(a, optimized)
a = example.copy()

experiment(a, best)
