def get_lis(a):
    if len(a) == 0:
        return []
    lis_len = 0
    lis = []
    for i in xrange(len(a)):
        b = []
        for j in xrange(i, len(a)):
            if a[i] < a[j]:
                b.append(a[j])
        lis_cand = [a[i]] + get_lis(b)
        if len(lis_cand) > lis_len:
            lis = lis_cand
            lis_len = len(lis)

    return lis


def get_inc_seq_list(seq):
    if len(seq) == 0:
        return []
    elif len(seq) == 1:
        return [[seq[0]]]

    is_list = []
    for i in xrange(len(seq)):
        is_list += [inc_seq for inc_seq in get_inc_seq_list(seq[i + 1:]) if inc_seq.insert(0, seq[i]) is None]

    return is_list


def get_jlis_len(a, b):
    a_list = get_inc_seq_list(a)
    b_list = get_inc_seq_list(b)


if __name__ == '__main__':
    c = int(raw_input())
    for i in xrange(c):
        a_len, b_len = (int(inp) for inp in raw_input().split())
        a = [int(inp) for inp in raw_input().split()]
        b = [int(inp) for inp in raw_input().split()]

        get_jlis_len(a, b)
