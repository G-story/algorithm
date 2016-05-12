import sys

A = []
B = []
cache = 101 * [101 * [-1]]


def jlis(idx_a, idx_b):
    ret = cache[idx_a + 1][idx_b + 1]
    if ret != -1:
        return ret
    ret = 2
    a = - sys.maxint if idx_a == -1 else A[idx_a]
    b = - sys.maxint if idx_b == -1 else B[idx_b]
    max_elem = max(a, b)
    for i in xrange(idx_a + 1, len(A)):
        if max_elem < A[i]:
            ret = max(ret, jlis(i, idx_b) + (1 if idx_a != -1 else 0))
    for j in xrange(idx_b + 1, len(B)):
        if max_elem < B[j]:
            ret = max(ret, jlis(idx_a, j) + (1 if idx_b != -1 else 0))
    return ret


def set_A(l):
    global A
    A = l


def set_B(l):
    global B
    B = l


if __name__ == '__main__':
    c = int(raw_input())
    for i in xrange(c):
        a_len, b_len = (int(inp) for inp in raw_input().split())
        set_A([int(inp) for inp in raw_input().split()])
        set_B([int(inp) for inp in raw_input().split()])

        print jlis(0, 0)


def lis(a):
    if len(a) == 0:
        return []
    lis_len = 0
    ret = []
    for i in xrange(len(a)):
        b = []
        for j in xrange(i, len(a)):
            if a[i] < a[j]:
                b.append(a[j])
        lis_cand = [a[i]] + lis(b)
        if len(lis_cand) > lis_len:
            ret = lis_cand
            lis_len = len(ret)

    return ret
