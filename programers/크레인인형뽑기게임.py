def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        index = move - 1
        for row in board:
            if row[index]:
                val = row[index]
                if stack and stack[-1] == val:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(val)
                row[index] = 0
                break
    return answer


if __name__ == '__main__':
    print(solution(
        [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
        [1, 5, 3, 5, 1, 2, 1, 4]
    ))
