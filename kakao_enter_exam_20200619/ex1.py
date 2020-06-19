from collections import defaultdict


def splitIntoTwo(arr):
    count = 0
    memo_left = defaultdict(int)
    memo_right = defaultdict(int)
    memo_right[-1] = sum(arr)
    for i in range(0, len(arr) - 1):
        left_sum, right_sum = memo_left[i - 1] + arr[i], memo_right[i - 1] - arr[i]
        memo_left[i], memo_right[i] = left_sum, right_sum
        if left_sum > right_sum:
            count += 1
    return count


if __name__ == '__main__':
    arr = [-3, -2, 10, 20, -30]
    result = splitIntoTwo(arr)
    print(result)
