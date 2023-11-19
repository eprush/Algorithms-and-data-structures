import time
import random


def example(n: int):
    begin, end = -100, 100
    return [random.randint(begin, end) for _ in range(n)]


def series(arr: list, funcs: list, ascending=True):
    def experiment(f):
        start = time.perf_counter()
        f(arr, ascending)
        t = (time.perf_counter() - start) * 10 ** 6
        print("Works in a", t, " mcs")
        print("The result is", arr)
        print()
        return

    old_arr = arr.copy()
    for func in funcs:
        experiment(func)
        arr = old_arr.copy()
    return
