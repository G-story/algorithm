import heapq


def find_n_largest_items_seq(seq, n):
    return heapq.nlargest(n, seq)


def find_n_largest_items_seq_sorted(seq, n):
    return sorted(seq)[-n:]


def find_n_smallest_items_seq(seq, n):
    return heapq.nsmallest(n, seq)


def find_n_smallest_items_seq_sorted(seq, n):
    return sorted(seq)[:n]


def find_smallest_items_seq(seq):
    return min(seq)


def find_smallest_items_seq_heap(seq):
    return heapq.heappop(seq)


def test_find_n_largest_smallest_items_seq():
    seq = [1, 3, 2, 8, 6, 10, 9]
    n = 3
    assert (find_n_largest_items_seq(seq, n) == [10, 9, 8])
    assert (find_n_largest_items_seq_sorted(seq, n) == [8, 9, 10])
    assert (find_n_smallest_items_seq(seq, n) == [1, 2, 3])
    assert (find_n_smallest_items_seq_sorted(seq, n) == [1, 2, 3])
    assert (find_smallest_items_seq(seq) == 1)
    assert (find_smallest_items_seq_heap(seq) == 1)

    print("테스트 통과!")


if __name__ == "__main__":
    test_find_n_largest_smallest_items_seq()
