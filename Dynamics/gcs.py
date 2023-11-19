from Tests.dynamics import gcs_example as example


def gcs(A: list, B: list):
    F = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    return F[-1][-1]


N, n = int(input()), int(input())
seq_1, seq_2 = example(N, n)
print(gcs(seq_1, seq_2))
