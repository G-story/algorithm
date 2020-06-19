from bisect import bisect_left


def searching_in_a_matrix(m, value):
    one_dim_m = [x for row in m for x in row]
    index = bisect_left(one_dim_m, value)
    return index < len(one_dim_m) and one_dim_m[index] == value


def test_searching_in_a_matrix():
    a = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
    b = [[1, 2], [3, 4]]
    assert (searching_in_a_matrix(a, 13) is True)
    assert (searching_in_a_matrix(a, 14) is False)
    assert (searching_in_a_matrix(b, 3) is True)
    assert (searching_in_a_matrix(b, 5) is False)
    print("테스트 통과!")


if __name__ == "__main__":
    test_searching_in_a_matrix()
