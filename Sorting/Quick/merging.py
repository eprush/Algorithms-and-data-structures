def simple(arr: list, ascending=True) -> None:
    sign = 2 * int(ascending) - 1

    def merge(arr_1: list, arr_2: list) -> list:
        res = [0] * (len(arr_1) + len(arr_2))
        i, j, n = 0, 0, 0
        while (i < len(arr_1)) and (j < len(arr_2)):
            # <= - because of stability
            if sign * arr_1[i] <= sign * arr_2[j]:
                res[n] = arr_1[i]
                i += 1
            else:
                res[n] = arr_2[j]
                j += 1
            n += 1

        while i < len(arr_1):
            res[n] = arr_1[i]
            i += 1
            n += 1

        while j < len(arr_2):
            res[n] = arr_2[j]
            j += 1
            n += 1
        return res

    def merge_sort(some_arr) -> None:
        if len(some_arr) <= 1:
            return

        middle = len(some_arr) // 2
        left_arr = some_arr[:middle]
        right_arr = some_arr[middle:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        res = merge(left_arr, right_arr)
        for i in range(len(some_arr)):
            some_arr[i] = res[i]
        return

    merge_sort(arr)
    return


def optimized(arr: list, ascending=True) -> None:
    sign = 2 * int(ascending) - 1

    def merge(some_arr: list, left: int, middle: int, right: int) -> None:
        buffer = [0] * (right - left)
        i, old_left, old_middle = 0, left, middle
        while (left < old_middle) and (middle < right):
            if sign * some_arr[left] <= sign * some_arr[middle]:
                buffer[i] = some_arr[left]
                left += 1
            else:
                buffer[i] = some_arr[middle]
                middle += 1
            i += 1

        while left < old_middle:
            buffer[i] = some_arr[left]
            left += 1
            i += 1
        while middle < right:
            buffer[i] = some_arr[middle]
            middle += 1
            i += 1

        for i in range(len(some_arr)):
            some_arr[i] = buffer[i - old_left]
        return

    def merge_sort(some_arr) -> None:
        if len(some_arr) <= 1:
            return

        left, middle, right = 0, len(some_arr) // 2, len(some_arr)
        L = some_arr[left: middle]
        R = some_arr[middle: right]
        merge_sort(L)
        merge_sort(R)
        res = L + R

        merge(res, left, middle, right)
        for i in range(len(some_arr)):
            some_arr[i] = res[i]
        return

    merge_sort(arr)
    return


if __name__ == "__main__":
    from Tests.sorting import series, example

    my_arr = example(int(input("The array lenght: ")))
    series(my_arr, [simple, optimized])
