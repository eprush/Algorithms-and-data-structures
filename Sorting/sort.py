import time
import random

def example(n : int):
    begin, end = -100, 100
    return [random.randint(begin, end) for _ in range(n)]

def series(arr: list, funcs: list):
    def experiment(func):
        start = time.perf_counter()
        func(arr)
        t = (time.perf_counter() - start) * 10 ** 6
        print("Works in a", t, " mcs")
        return

    old_arr = arr.copy()
    for func in funcs:
        experiment(func)
        arr = old_arr.copy()
    return
