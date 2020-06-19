from bisect import bisect, bisect_left


def find_time_occurrence_list(seq, k):
    return bisect(seq, k) - bisect_left(seq, k)


def test_find_time_occurrence_list():
    seq = [1, 2, 2, 2, 2, 2, 2, 5, 6, 6, 7, 8, 9]
    k = 2
    assert (find_time_occurrence_list(seq, k) == 6)
    print("테스트 통과!")


if __name__ == "__main__":
    test_find_time_occurrence_list()
