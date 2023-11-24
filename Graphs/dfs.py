from adj_list import adj_list, n

used = [False] * n


def start_over():
    for i in range(n):
        used[i] = False
    return


def dfs(u: int):
    used[u] = True
    for v in adj_list[u]:
        if not used[v]:
            dfs(v)
    return


def bypass_graph():
    for u in range(n):
        if not used[u]:
            dfs(u)
