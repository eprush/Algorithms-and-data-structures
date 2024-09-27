def simple(arr: list, ascending=True) -> None:
    sign = 2 * int(ascending) - 1
    for _ in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if sign * arr[j] > sign * arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return


def optimized(arr: list, ascending=True):
    sign = 2 * int(ascending) - 1
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if sign * arr[j] > sign * arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return


def best(arr: list, ascending=True):
    # if internal loop hasn't swapping,
    # there is a time to stop
    i = 0
    sign = 2 * int(ascending) - 1
    swapping = True
    while swapping:
        swapping = False
        for j in range(len(arr) - i - 1):
            if sign * arr[j] > sign * arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapping = True
        i += 1
    return


if __name__ == "__main__":
    from Tests.sorting import series, example

    my_arr = example(int(input("The array lenght: ")))
    series(my_arr, [simple, optimized, best])
