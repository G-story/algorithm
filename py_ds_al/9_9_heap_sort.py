import heapq


def heap_sort(seq):
    h = seq.copy()
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


def test_heap_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert (heap_sort(seq) == sorted(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_heap_sort()
