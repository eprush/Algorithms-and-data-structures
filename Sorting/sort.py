import time


def experiment(arr: list, func):
    start = time.perf_counter()
    func(arr)
    t = (time.perf_counter() - start) * 10 ** 6
    print("Works in a", t, " mcs")
    return
