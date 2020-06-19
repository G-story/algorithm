def selection_sort(seq):
    for i in range(len(seq) - 1):
        min_index, min_value = min(enumerate(seq[i:]), key=lambda x: x[1])
        seq[i], seq[i + min_index] = min_value, seq[i]
    return seq


def test_selection_sort():
    seq = [11, 3, 28, 43, 9, 4]
    assert (selection_sort(seq) == sorted(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_selection_sort()
