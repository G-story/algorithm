import sys

INF = 987654321
N = ''


def classify(a, b):
    M = N[a:b + 1]
    if M == len(M) * M[0]:
        return 1
    progressive = True
    for i in range(len(M) - 1):
        if int(M[i + 1]) - int(M[i]) != int(M[1]) - int(M[0]):
            progressive = False
    if progressive and abs(int(M[1]) - int(M[0])) == 1:
        return 2
    alternating = True
    for i in range(len(M)):
        if M[i] != M[i % 2]:
            alternating = False
    if alternating:
        return 4
    if progressive:
        return 5
    return 10


cache = 10002 * [None]


def memorize(begin):
    if begin == len(N):
        return 0
    ret = cache[begin]
    if ret != None:
        return ret
    ret = INF
    for L in range(3, 6):
        if begin + L <= len(N):
            ret = min(ret, memorize(begin + L) + classify(begin, begin + L - 1))
    cache[begin] = ret
    return ret


def execute(caseCnt, nums=None):
    global N
    global cache
    ret = []
    for i in range(caseCnt):
        if nums == None:
            N = input()
        else:
            N = nums[i]
        min_difficulty = memorize(0)
        cache = 10002 * [None]
        print(min_difficulty)
        ret += [min_difficulty]
    return ret


if __name__ == '__main__':
    sys.setrecursionlimit(3000)
    caseCnt = int(input())
    execute(caseCnt)
