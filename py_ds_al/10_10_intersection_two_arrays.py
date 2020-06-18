from bisect import bisect_left


def intersection_two_arrays_sets(seq1, seq2):
    return set(seq1) & set(seq2)


def intersection_two_arrays_bs(seq1, seq2):
    result = set()
    if len(seq1) <= len(seq1):
        base_seq, target_seq = seq1, seq2
    else:
        base_seq, target_seq = seq2, seq1
    for x in base_seq:
        i = bisect_left(target_seq, x)
        if i < len(target_seq) and x == target_seq[i]:
            result.add(x)
    return result


def test_intersection_two_arrays():
    seq1 = [1, 2, 3, 5, 7, 8]
    seq2 = [3, 5, 6]
    assert (intersection_two_arrays_sets(seq1, seq2) == set([3, 5]))
    assert (intersection_two_arrays_bs(seq1, seq2) == set([3, 5]))
    print("테스트 통과!")


if __name__ == "__main__":
    test_intersection_two_arrays()
