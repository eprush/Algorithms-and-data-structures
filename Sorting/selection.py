from Tests.sorting import series, example


def simple(arr: list, ascending=True):
    sign = 2 * int(ascending) - 1
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if sign*arr[i] > sign*arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return


def best(arr: list, ascending=True):
    sign = 2 * int(ascending) - 1
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if sign*arr[min_index] > sign*arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return


my_arr = example(100)
series(my_arr, [simple, best])
