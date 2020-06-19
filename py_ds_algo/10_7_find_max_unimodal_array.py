def find_max_unimodal_array(seq):
    i = len(seq) // 2
    val, left, right = seq[i], seq[:i - 1], seq[i + 1:]
    if val < left[-1]:
        for j in range(i, 0, -1):
            if seq[j] > seq[j - 1]:
                return seq[j]
    elif val < right[0]:
        for j in range(i, len(seq) - 1):
            if seq[j] > seq[j + 1]:
                return seq[j]
    else:
        return val


def test_find_max_unimodal_array():
    seq = [1, 2, 5, 6, 7, 10, 12, 9, 8, 7, 6]
    assert (find_max_unimodal_array(seq) == max(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_find_max_unimodal_array()
