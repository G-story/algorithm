# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
def solution(N, stages):
    answer = []
    f_rates = []
    for i in range(1, N + 1):
        cand_cnt = len([x for x in stages if x >= i])
        fail_cnt = len([x for x in stages if x == i])
        f_rate = fail_cnt / cand_cnt if cand_cnt > 0 else 0
        f_rates.append([f_rate, i])
    answer = [i for f_rate, i in sorted(f_rates, key=lambda x: x[0], reverse=True)]
    return answer


if __name__ == '__main__':
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
