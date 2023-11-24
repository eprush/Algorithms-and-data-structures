from Tests.sorting import series, example


# version uses additional memory
def simple(arr: list, ascending=True) -> None:
    sign = 2 * int(ascending) - 1

    def hoar_sort(some_arr):
        if len(some_arr) <= 1:
            return

        barrier = some_arr[0]
        L, M, R = [], [], []
        for element in some_arr:
            if sign * element < sign * barrier:
                L.append(element)
            elif element == barrier:
                M.append(element)
            else:
                R.append(element)
        hoar_sort(L)
        hoar_sort(R)
        i = 0
        for element in L + M + R:
            some_arr[i] = element
            i += 1
        return

    hoar_sort(arr)
    return


# in-place version
def optimized(arr: list, ascending=True) -> None:
    # incorrect code
    sign = 2 * int(ascending) - 1

    def hoar_sort(begin=0, end=len(arr) - 1):
        if end - begin <= 1:
            return

        i, j, = begin, end
        barrier = arr[begin]
        while i <= j:
            while sign * arr[i] < sign * barrier:
                i += 1
            while sign * arr[j] > sign * barrier:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        hoar_sort(begin, j)
        hoar_sort(i, end)
        return
    hoar_sort()
    return
