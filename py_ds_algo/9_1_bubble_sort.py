def bubble_sort(seq):
    for n in range(len(seq) - 1, 0, -1):
        for i in range(n):
            curr, next = seq[i], seq[i + 1]
            if curr > next:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    return seq


def test_bubble_sort():
    seq = [11, 3, 28, 43, 9, 4]
    assert (bubble_sort(seq) == sorted(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_bubble_sort()
