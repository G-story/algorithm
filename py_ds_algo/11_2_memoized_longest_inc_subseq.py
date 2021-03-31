from bisect import bisect

from benchmark import benchmark


def longest_inc_subseq(s1):
    arr = []
    for x in s1:
        index = bisect(arr, x)
        if index == len(arr):
            arr.append(x)
        else:
            arr[index] = x
    return len(arr)


@benchmark
def test_longest_inc_subseq():
    print(longest_inc_subseq(s1))


if __name__ == "__main__":
    from random import randrange
    s1 = [randrange(100) for i in range(10000)]
    # s1 = [94, 8, 78, 22, 38, 79, 93, 8, 84, 39]
    print(s1)
    test_longest_inc_subseq()
