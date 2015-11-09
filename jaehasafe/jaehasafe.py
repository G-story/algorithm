def get_index_of_substring(origin, substring):
    for i in range(len(origin)):
        if origin[i] == substring[0]:
            is_match = True
            dup_str = origin[i]
            prefix = ''
            suffix = ''
            dup_str2 = ''
            for j in range(1, len(substring)):
                dup_str += substring[j]
                if origin[i + j] != substring[j]:
                    is_match = False
                    dup_str_last_idx = len(dup_str) - 1
                    for k in range(dup_str_last_idx):
                        prefix += dup_str[k]
                        suffix = dup_str[dup_str_last_idx - k] + suffix
                        if prefix == suffix:
                            dup_str2 = prefix
                    if len(dup_str2) > 0:
                        i += len(dup_str) - len(dup_str2) - 1
                    break
            if is_match:
                return i


def get_min_dial_cnt(states):
    min_dial_cnt = 0

    for i in range(len(states) - 1):
        if i % 2 == 0:
            min_dial_cnt += get_index_of_substring(states[i + 1] + states[i + 1], states[i])
        else:
            min_dial_cnt += get_index_of_substring(states[i] + states[i], states[i + 1])

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
