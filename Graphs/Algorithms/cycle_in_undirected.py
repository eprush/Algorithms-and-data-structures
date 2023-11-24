from enum import IntEnum
from Graphs.Storages.adj_list import adj_list, n
from dfs import used


class Colors(IntEnum):
    WHITE = 0
    GREY = 1
    BLACK = 2


for i in range(n):
    used[i] = Colors.WHITE


def is_cycle_found(current: int):

    used[current] = Colors.GREY
    for child in adj_list[current]:
        if used[child] == Colors.WHITE:
            if is_cycle_found(child):
                return True
        elif used[child] == Colors.GREY:
            return True

    used[current] = Colors.BLACK
    return False


def is_cycle_graph():
    for u in range(n):
        if used[u] == Colors.WHITE and is_cycle_found(u):
            return True
    return False


if __name__ == "__main__":
    ans = " " if is_cycle_graph() else " no "
    print("Graph has{}cycle".format(ans))
