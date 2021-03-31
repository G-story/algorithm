from collections import defaultdict


def count_sort(seq):
    count_dict, result = defaultdict(list), []
    for x in seq:
        count_dict[x].append(x)
    for i in range(min(count_dict), max(count_dict) + 1):
        result += count_dict[i]
    return result


def test_count_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
    assert (count_sort(seq) == sorted(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_count_sort()
