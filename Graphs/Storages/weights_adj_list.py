def create(verticles: int):
    return [set() for _ in range(verticles)]


def fill_undirected(verts: int, edges: int):
    adj_l = create(verts)
    for _ in range(edges):
        u, v, w = map(int, input("from to weights: ").split())
        adj_l[u].add((v, w))
        adj_l[v].add((u, w))
    return adj_l


def fill_directed(verts: int, edges: int):
    adj_l = create(verts)
    for _ in range(edges):
        u, v, w = map(int, input("from to weights: ").split())
        adj_l[u].add((v, w))
    return adj_l


print("Do you want undirected graph? ")
is_undirected = input() == "yes"
n, m = map(int, input("verticles  edges: ").split())
adj_list = fill_undirected(n, m) if is_undirected else fill_directed(n, m)
