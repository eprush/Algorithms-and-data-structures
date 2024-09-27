def find_gis(arr: list):
    def init_extreme_case():
        return [0] * (len(arr) + 1)
    great_increasing_len = init_extreme_case()

    def max_of_previous(pos):
        maximum = 0
        for j in range(pos):
            if arr[pos] > arr[j] and great_increasing_len[j + 1] > maximum:
                maximum = great_increasing_len[j + 1]
        return maximum

    for i in range(len(arr)):
        great_increasing_len[i+1] = max_of_previous(i) + 1
    return max(*great_increasing_len)


if __name__ == "__main__":
    from Tests.dynamics import gis_example as create_example
    from Sorting.Quick.hoar import simple as hoar_sort
    N = int(input())
    my_arr = create_example(N)
    print(my_arr)
    print(find_gis(my_arr))

    hoar_sort(my_arr)
    print(my_arr)
    print(find_gis(my_arr))
