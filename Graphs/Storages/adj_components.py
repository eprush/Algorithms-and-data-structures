from adj_list import adj_list, n
from dfs import dfs as usual_dfs
from dfs import start_over, used

comps = []


def dfs(u):
    comps.append(u)
    used[u] = True
    for v in adj_list[u]:
        if not used[v]:
            dfs(v)
    return


def count_comps():
    count = 0
    for u in range(n):
        if not used[u]:
            count += 1
            usual_dfs(u)
    return count


def print_comps():
    print("Graph has the next adj components")
    for u in range(n):
        if not used[u]:
            comps.clear()
            dfs(u)
            print(*comps)
    return


if __name__ == "__main__":
    print("Graph has {} adj components".format(count_comps()),  "\n")
    start_over()
    print_comps()
