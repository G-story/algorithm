from collections import Counter


def solution(answers):
    counter = Counter()
    people_board = [
        (len(answers) // 5) * [1, 2, 3, 4, 5] + [1, 2, 3, 4, 5][:len(answers) % 5],
        (len(answers) // 8) * [2, 1, 2, 3, 2, 4, 2, 5] + [2, 1, 2, 3, 2, 4, 2, 5][:len(answers) % 8],
        (len(answers) // 10) * [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] + [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][:len(answers) % 10],
    ]
    for i, x in enumerate(answers):
        for j, person_board in enumerate(people_board):
            if person_board[i] == x:
                counter[j + 1] += 1
    max_cnt = counter.most_common(1)[0][1]
    answer = sorted([person_num for person_num, count in counter.most_common(3) if count == max_cnt])

    return answer


if __name__ == '__main__':
    print(solution([1, 3, 2, 4, 2]))
