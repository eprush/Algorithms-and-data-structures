def create(verticles: int):
    return [[] for _ in range(verticles)]


def fill_undirected(vert: int, edges: int):
    adj_l = create(vert)
    for _ in range(edges):
        u, v = map(int, input("from to: ").split())
        adj_l[u].append(v)
        adj_l[v].append(u)
    return adj_l


def fill_directed(vert: int, edges: int):
    adj_l = create(vert)
    for _ in range(edges):
        u, v = map(int, input("from to: ").split())
        adj_l[u].append(v)
    return adj_l


print("Do you want undirected graph? ")
if __name__ == "cycle_in_undirected":
    is_undirected = True
elif __name__ == "cycle_in_directed":
    is_undirected = False
else:
    is_undirected = input() == "yes"
n, m = map(int, input("verticles  edges: ").split())
adj_list = fill_undirected(n, m) if is_undirected else fill_directed(n, m)
