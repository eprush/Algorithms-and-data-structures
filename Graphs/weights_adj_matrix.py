def create(verticles: int):
    return [[float("inf")] * verticles for _ in range(verticles)]


def fill_undirected(vert: int, edges: int):
    matrix = create(vert)
    for _ in range(edges):
        u, v, w = map(int, input("from to weights: ").split())
        matrix[u][v] = min(matrix[u][v], w)
        matrix[v][u] = min(matrix[v][u], w)
    for i in range(vert):
        matrix[i][i] = 0
    return matrix


def fill_directed(vert: int, edges: int):
    matrix = create(vert)
    for _ in range(edges):
        u, v, w = map(int, input("from to weights: ").split())
        matrix[u][v] = min(matrix[u][v], w)
    for i in range(vert):
        matrix[i][i] = 0
    return matrix


print("Do you want undirected graph?")
is_undirected = input() == "yes"
n, m = map(int, input("verticles  edges: ").split())
adj_matrix = fill_undirected(n, m) if is_undirected else fill_directed(n, m)
