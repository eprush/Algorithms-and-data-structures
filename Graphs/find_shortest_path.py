from queue import SimpleQueue
from adj_list import adj_list, n


def find_all_dists_from(start: int):
    def init_state():
        return [0 if i == start else float("inf") for i in range(n)]

    distances = init_state()
    q = SimpleQueue()
    q.put(start)

    def bypass():
        while not q.empty():
            current = q.get()
            for child in adj_list[current]:
                if distances[child] == float("inf"):
                    q.put(child)
                    distances[child] = distances[current] + 1
        return

    bypass()
    return distances


def find_shortest_path(start: int, target: int):
    def init_state():
        return [0 if i == start else float("inf") for i in range(n)]

    def process_current():
        for child in adj_list[current]:
            if distances[child] == float("inf"):
                q.put(child)
                distances[child] = distances[current] + 1
                ancestors[child] = current
        return

    distances = init_state()
    ancestors = [None] * n
    q = SimpleQueue()
    q.put(start)
    while not q.empty():
        current = q.get()
        process_current()

    def restore_path():
        path = []
        end = target
        while end is not None:
            path.append(end)
            end = ancestors[end]
        return path[::-1]

    return restore_path()


if __name__ == "__main__":
    print("Do you want to find the shortest path or all distances? ")
    ans = input()
    if ans == "all distances":
        s = int(input("start from: "))
        print(find_all_dists_from(s))
    elif ans == "the shortest path":
        s, t = map(int, input("start_from to: ").split())
        print(find_shortest_path(s, t))
