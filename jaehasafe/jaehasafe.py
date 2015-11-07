def get_min_dial_cnt(states):
    min_dial_cnt = 0

    for i in range(len(states) - 1):
        if i % 2 == 0:
            min_dial_cnt += (states[i + 1] + states[i + 1]).find(states[i])
        else:
            min_dial_cnt += (states[i] + states[i]).find(states[i + 1])

    return min_dial_cnt


def in_out():
    N = int(input())
    states = []
    for i in range(N + 1):
        states += [input()]
    res = get_min_dial_cnt(states)
    print(res)


if __name__ == '__main__':
    C = int(input())

    for i in range(C):
        in_out()
