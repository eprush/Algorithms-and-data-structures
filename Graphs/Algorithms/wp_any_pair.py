from Graphs.Storages.weights_adj_matrix import adj_matrix, n


# the Floyd-Warshell algorithm
def find_paths():
    for intermediate_vert in range(n):
        for vert_1 in range(n):
            for vert_2 in range(n):
                adj_matrix[vert_1][vert_2] = min(adj_matrix[vert_1][vert_2],
                                                 adj_matrix[vert_1][intermediate_vert] +
                                                 adj_matrix[intermediate_vert][vert_2])
    return


if __name__ == "__main__":
    find_paths()
    for line in adj_matrix:
        print(*line)
