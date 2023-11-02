from sort import series, example


def simple(arr: list, ascending=True):
    for i in range(1, len(arr)):
        j = i - 1
        while (j >= 0) and (arr[j] > arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1

    if not ascending:
        arr.reverse()
    return


my_arr = example(10)
series(my_arr, [simple])