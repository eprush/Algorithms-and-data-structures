def simple(arr: list, ascending=True):
    sign = 2 * int(ascending) - 1
    for i in range(1, len(arr)):
        j = i - 1
        while (j >= 0) and (sign * arr[j] > sign * arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return


if __name__ == "__main__":
    from Tests.sorting import series, example

    my_arr = example(int(input("The array lenght: ")))
    series(my_arr, [simple])
