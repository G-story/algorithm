from bisect import bisect


def find_elem_matrix_bool(m, value):
    m_rotated = list(zip(*m))
    row, x_last, y_first = m[0], len(m[0]) - 1, 0
    while x_last >= 0 and y_first >= 0:
        x_last = bisect(row[:x_last + 1], value) - 1
        if value == row[x_last]:
            return True
        row = m_rotated[x_last]
        y_first = bisect(row[y_first:], value) - 1
        if value == row[y_first]:
            return True
        row = m[y_first + 1]

    return False


def test_find_elem_matrix_bool():
    m1 = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    assert (find_elem_matrix_bool(m1, 8) is True)
    assert (find_elem_matrix_bool(m1, 3) is False)
    m2 = [[0]]
    assert (find_elem_matrix_bool(m2, 0) is True)
    print("테스트 통과!")


if __name__ == "__main__":
    test_find_elem_matrix_bool()
