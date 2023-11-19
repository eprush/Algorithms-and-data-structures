from .search import example as search_example


def gcs_example(N: int, n: int):
    common_seq = search_example(n)
    res_1 = search_example(N) + common_seq
    res_2 = common_seq + search_example(N)
    return res_1, res_2


def gis_example(N: int):
    return search_example(N)
