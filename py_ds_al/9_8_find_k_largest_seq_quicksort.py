def find_k_largest_seq_quickselect(seq, k):
    ipivot = len(seq) // 2
    pivot = seq[ipivot]
    left = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    right = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]
    rank = len(right) + 1
    if rank == k:
        return [pivot] + right
    elif rank < k:
        return find_k_largest_seq_quickselect(left, k - 1 - len(right)) + [pivot] + right
    else:
        return find_k_largest_seq_quickselect(right, k)


if __name__ == "__main__":
    seq = [3, 10, 4, 5, 1, 8, 9, 11, 5]
    k = 3
    print(find_k_largest_seq_quickselect(seq, k))
