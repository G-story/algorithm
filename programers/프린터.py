def solution(priorities, location):
    answer = 0
    while priorities:
        if priorities[0] == max(priorities):
            priorities.pop(0)
            answer += 1
            if location == 0:
                return answer
            else:
                location -= 1
        else:
            priorities = priorities[1:] + priorities[0:1]
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1


if __name__ == '__main__':
    print(solution([1, 1, 9, 1, 1, 1], 0))
