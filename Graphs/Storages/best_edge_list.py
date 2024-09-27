from edge_list import fill_directed_list as fill_directed
from edge_list import fill_undirected_list as fill_undirected


def improve(edges: list):
    edges.sort()


if "__name__" == "__main__":
    print("Do you want create the undirected graphs?")
    ans = input()
    n, m = map(int, input("verticles  edges:").split())
    if ans == "YES":
        e = fill_undirected(m)
    else:
        e = fill_directed(m)
    improve(e)
