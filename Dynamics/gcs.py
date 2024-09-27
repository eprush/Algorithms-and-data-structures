def find_gcs(A: list, B: list):
    def init_extreme_case():
        return [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

    common_seq_len = init_extreme_case()

    def next_len(pos_1: int, pos_2: int):
        if A[pos_1] == B[pos_2]:
            common_seq_len[pos_1 + 1][pos_2 + 1] = 1 + common_seq_len[pos_1][pos_2]
        else:
            common_seq_len[pos_1 + 1][pos_2 + 1] = max(common_seq_len[pos_1][pos_2 + 1],
                                                       common_seq_len[pos_1 + 1][pos_2])
        return

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            next_len(i - 1, j - 1)
    return common_seq_len[-1][-1]


if __name__ == "__main__":
    from Tests.dynamics import gcs_example as create_example
    N, n = int(input()), int(input())
    seq_1, seq_2 = create_example(N, n)
    print(seq_1, seq_2)
    print(find_gcs(seq_1, seq_2))
