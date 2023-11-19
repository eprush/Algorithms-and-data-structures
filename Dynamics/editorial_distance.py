def find_dist(A: str, B: str):
    def init_extreme_case():
        return [[(a + b) if a * b == 0 else 0 for b in range(len(B) + 1)]
                for a in range(len(A) + 1)]

    editorial_dists = init_extreme_case()

    def next_dist(pos_1, pos_2, dists):
        if A[pos_1 - 1] == B[pos_2 - 1]:
            dists[pos_1][pos_2] = dists[pos_1 - 1][pos_2 - 1]
        else:
            change, add, delete = (dists[pos_1 - 1][pos_2 - 1],
                                   dists[pos_1][pos_2 - 1],
                                   dists[pos_1 - 1][pos_2])
            dists[pos_1][pos_2] = 1 + min(change, add, delete)
        return

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            next_dist(i, j, editorial_dists)
    return editorial_dists[-1][-1]
