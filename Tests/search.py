import time
import random


def example(n: int):
    begin, end = -100, 100
    return [random.randint(begin, end) for _ in range(n)]


def series(arr: list, funcs: list, key):
    def experiment(f):
        start = time.perf_counter()
        res = f(arr, key)
        t = (time.perf_counter() - start) * 10 ** 6
        print("Works in a", t, " mcs")
        print("The result is", res)
        print()
        return

    old_arr = arr.copy()
    for func in funcs:
        experiment(func)
    return
