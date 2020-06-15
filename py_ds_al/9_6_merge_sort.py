def merge_sort(seq):
    if len(seq) == 1:
        return seq
    result = []
    seq1, seq2 = seq[:len(seq) // 2], seq[len(seq) // 2:]
    sorted1, sorted2 = merge_sort(seq1), merge_sort(seq2)
    i1, i2 = 0, 0
    while i1 < len(sorted1) and i2 < len(sorted2):
        if sorted1[i1] < sorted2[i2]:
            result.append(sorted1[i1])
            i1 += 1
        else:
            result.append(sorted2[i2])
            i2 += 1
    result += sorted1[i1:] + sorted2[i2:]
    return result


def test_merge_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    seq_sorted = sorted(seq)
    assert (merge_sort(seq) == seq_sorted)
    print("테스트 통과!")


if __name__ == "__main__":
    test_merge_sort()
