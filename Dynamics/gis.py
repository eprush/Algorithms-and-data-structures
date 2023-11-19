from Tests.dynamics import gis_example as example
from Sorting.hoar import simple as hoar_sort


def gis(arr: list):
    F = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        maximum = 0
        for j in range(i):
            if arr[i] > arr[j] and F[j+1] > maximum:
                maximum = F[j+1]
        F[i+1] = maximum + 1
    return max(*F)


N = int(input())
my_arr = example(N)
print(my_arr)
print(gis(my_arr))

hoar_sort(my_arr)
print(my_arr)
print(gis(my_arr))
