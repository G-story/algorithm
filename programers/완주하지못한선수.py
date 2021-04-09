from collections import Counter


def solution(participant, completion):
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    answer = next((p_counter - c_counter).elements())
    return answer


if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
