from Tests.search import series, example
from Sorting.hoar import simple


def linear_search(arr: list, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    error_note = -1
    return error_note


my_arr = example(1000)
print(my_arr)
number = int(input())
series(my_arr, [linear_search], number)
