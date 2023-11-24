from edge_list import fill_directed_list as fill_directed
from edge_list import fill_undirected_list as fill_undirected


def fill_directed_list(edges: int):
    edge_list = fill_directed(edges)
    edge_list.sort()
    return edge_list


def fill_undirected_list(edges: int):
    edge_list = fill_undirected(edges)
    edge_list.sort()
    return edge_list

if "__name__" == "__main__":
    print("Do you want create the undirected graphs?")
    ans = input()
    n, m = map(int, input("verticles  edges:").split())
    if ans == "YES":
        adj_m = fill_undirected_list(m)
    else:
        adj_m = fill_directed_list(m)