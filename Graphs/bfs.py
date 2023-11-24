from queue import SimpleQueue
from adj_list import adj_list, n

used = [False] * n


def start_over():
    for i in range(n):
        used[i] = False
    return


def bfs(start: int):
    q = SimpleQueue()
    q.put(start)
    while not q.empty():
        current = q.get()
        for child in adj_list[current]:
            if not used[child]:
                q.put(child)
    return
