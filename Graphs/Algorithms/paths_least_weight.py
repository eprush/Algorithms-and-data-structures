from Graphs.Storages.weights_adj_list import adj_list, n


# Dijkstra 's algorithm
def find_paths(start: int):
    def init_state():
        return [0 if i == start else float("inf") for i in range(n)]
    distances = init_state()
    used = [False] * n

    def find_min_unused():
        u = -1
        for i in range(n):
            if not used[i] and (u == -1 or distances[i] < distances[u]):
                u = i
        return u

    def fill_dists(u: int):
        for v, w in adj_list[u]:
            distances[v] = min(distances[v], distances[u] + w)
        return

    def bypass():
        for _ in range(n):
            current = find_min_unused()
            if distances[current] == float("inf"):
                break
            used[current] = True
            fill_dists(current)
        return

    bypass()
    return distances


if __name__ == "__main__":
    s = int(input("Start from: "))
    print(find_paths(s))
