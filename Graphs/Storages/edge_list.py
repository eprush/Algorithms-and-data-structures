def create(edges: int) -> list:
    return [(0, 0)] * edges


def fill_undirected_list(edges: int) -> list:
    edge_list = []
    for i in range(edges):
        u, v = map(int, input().split())
        edge_list.append((u, v))
        edge_list.append((v, u))
    return edge_list


def fill_directed_list(edges: int) -> list:
    edge_list = create(edges)
    for i in range(edges):
        u, v = map(int, input().split())
        edge_list.append((u, v))
    return edge_list


if "__name__" == "__main__":
    print("Do you want create the undirected graphs?")
    ans = input()
    n, m = map(int, input("verticles  edges:").split())
    if ans == "YES":
        e = fill_undirected_list(m)
    else:
        e = fill_directed_list(m)
