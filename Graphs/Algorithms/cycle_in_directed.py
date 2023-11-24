from Graphs.Storages.adj_list import adj_list, n
from dfs import used

is_cycle_found = False
end_of_cycle = -1


def dfs(current: int, previous: int):
    def do_iteration(v: int):
        global is_cycle_found
        global end_of_cycle
        if is_cycle_found:
            return
        if not used[v]:
            dfs(v, current)
        elif v != previous:
            is_cycle_found = True
            end_of_cycle = v
        return

    def end_finding():
        if is_cycle_found:
            print(current, end=" ")
        if current == end_of_cycle:
            exit()
        return

    used[current] = True
    for child in adj_list[current]:
        do_iteration(child)
    end_finding()
    return


def is_cycle_graph():
    for u in range(n):
        if not used[u]:
            dfs(u, -1)
    print()
    return


if __name__ == "__main__":
    is_cycle_graph()
    ans = " " if is_cycle_found else " no "
    print("Graph has{}cycle".format(ans))
