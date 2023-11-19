from Tests.search import series, example
from Sorting.hoar import simple


# if only one element, which equal key,  exists, return his index
# if element, which equal key, doesn't exist, return error note
# if there are many elements, which equal key, return left and right boundaries
def bin_search(arr: list, key):
    def left_bound():
        left = -1
        right = len(arr)
        while right - left > 1:
            middle = (right + left) // 2
            if arr[middle] < key:
                left = middle
            else:
                right = middle
        return left

    def right_bound():
        left = -1
        right = len(arr)
        while right - left > 1:
            middle = (right + left) // 2
            if arr[middle] <= key:
                left = middle
            else:
                right = middle
        return right

    left, right = left_bound(), right_bound()
    error_note = -1
    if right - left == 2:
        return left + 1
    elif right - left > 2:
        return left, right
    return error_note


my_arr = example(1000)
simple(my_arr)
print(my_arr)
number = int(input())
series(my_arr, [bin_search], number)
