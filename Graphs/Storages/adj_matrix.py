def create(verticles: int):
    return [[0] * verticles for _ in range(verticles)]


def fill_undirected_matrix(vert: int, edges: int):
    matrix = create(vert)
    for _ in range(edges):
        u, v = map(int, input().split())
        matrix[u][v] = 1
        matrix[v][u] = 1
    return matrix


def fill_directed_matrix(vert: int, edges: int):
    matrix = create(vert)
    for _ in range(edges):
        u, v = map(int, input().split())
        matrix[u][v] = 1
    return matrix


print("Do you want create the undirected graphs?")
ans = input()
n, m = map(int, input("verticles  edges:").split())
if ans == "YES":
    adj_m = fill_undirected_matrix(n, m)
else:
    adj_m = fill_directed_matrix(n, m)

