from itertools import combinations


def solution(numbers):
    answer = sorted(list(set(sum(x) for x in combinations(numbers, 2))))
    return answer


if __name__ == '__main__':
    print(solution([2, 1, 3, 4, 1]))
