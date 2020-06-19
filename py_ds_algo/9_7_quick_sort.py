def partition(seq, start, end):
    pivot = seq[(start + end) // 2]

    while start <= end:
        while seq[start] < pivot:
            start += 1
        while seq[end] > pivot:
            end -= 1
        if start > end:
            break
        seq[start], seq[end] = seq[end], seq[start]
        start += 1
        end -= 1
    return start


def quick_sort(seq, start, end):
    p = partition(seq, start, end)
    if start < end:
        quick_sort(seq, start, p - 1)
        quick_sort(seq, p, end)
    return seq


def quick_sort_cache(seq):
    if len(seq) < 2:
        return seq
    ipivot = len(seq) // 2
    pivot = seq[ipivot]

    left = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    right = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]
    return quick_sort_cache(left) + [pivot] + quick_sort_cache(right)


def test_quick_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert (quick_sort(seq, 0, len(seq) - 1) == sorted(seq))
    assert (quick_sort_cache(seq) == sorted(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_quick_sort()
