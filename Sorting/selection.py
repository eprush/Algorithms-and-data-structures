from sort import series, example


def simple(arr: list, ascending=True):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    if not ascending:
        arr.reverse()
    return


def best(arr: list, ascending=True):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]

    if not ascending:
        arr.reverse()
    return


my_arr = example(10)
series(my_arr, [simple, best])
