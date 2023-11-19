from Tests.sorting import series, example


def build_heap(heap):
    n = len(heap)
    for i in range(n // 2, -1, -1):
        sift_down(heap, i)
    return


def sift_down(heap, pos):
    while True:
        j = pos

        if 2 * pos + 1 < len(heap) and heap[2 * pos + 1] < heap[pos]:
            j = 2 * pos + 1
        if 2 * j + 2 < len(heap) and heap[2 * pos + 2] < heap[pos]:
            j = 2 * pos + 2
        if j == pos:
            return

        heap[pos], heap[j] = heap[j], heap[pos]
        sift_down(heap, pos)
        pos = j


# version uses additional memory
def simple(arr: list, ascending=True):
    heap = arr.copy()
    build_heap(heap)
    n = len(heap)
    for i in range(len(arr)):
        heap[0], heap[n - 1] = heap[n - 1], heap[0]
        arr[i] = heap.pop()
        n -= 1
        sift_down(heap, 0)

    if not ascending:
        arr.reverse()
    return


# in-place version
def optimized(arr: list, ascending=True) -> None:
    if not ascending:
        arr.reverse()
    return


my_arr = example(100)
print(my_arr)
series(my_arr, [simple, optimized])
