# if only one element, which equal key,  exists, return his index
# if element, which equal key, doesn't exist, return error note
# if there are many elements, which equal key, return left and right boundaries
def bin_search(arr: list, key):
    def find_bound():
        left = -1
        right = len(arr)
        while right - left > 1:
            middle = (right + left) // 2
            if arr[middle] < key:
                left = middle
            else:
                right = middle
        return left, right

    l, r = find_bound()
    error_note = -1
    if r - l == 2:
        return l + 1
    elif r - l > 2:
        return l, r
    return error_note


if __name__ == "__main__":
    from Tests.search import series, example
    from Sorting.Quick.hoar import simple

    my_arr = example(1000)
    simple(my_arr)
    print(my_arr)
    number = int(input())
    series(my_arr, [bin_search], number)
