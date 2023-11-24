from Graphs.Storages.weights_adj_list import adj_list, n


# Prim 's algorithm
def find_min_st(start: int = 0):
    S = {start}
    spanning_tree, st_weight = [], 0

    def find_edge():
        min_weight, e = float("inf"), None
        for u in S:
            for v, w in adj_list[u]:
                if v not in S and w < min_weight:
                    min_weight = w
                    e = (u, v, w)
        return e, min_weight

    for _ in range(n-1):
        edge, weight = find_edge()
        if weight < float("inf"):
            S.add(edge[1])
            st_weight += weight
            spanning_tree.append(edge)

    print("The weight of spanning tree equals", st_weight)
    print("The spanning tree is", *spanning_tree, sep="\n")
    return


if __name__ == "__main__":
    find_min_st()
