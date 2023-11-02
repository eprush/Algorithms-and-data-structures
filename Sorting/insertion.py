from sort import experiment


def simple(arr: list, ascending=True):
    for i in range(1, len(arr)):
        j = i - 1
        while (j >= 0) and (arr[j] > arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1

    if not ascending:
        arr.reverse()
    return


example = [-1, 1, 0, 1, 2, -10, -2, 0, 10]
print("The lenght of example array equals", len(example))
a = example.copy()

experiment(a, simple)