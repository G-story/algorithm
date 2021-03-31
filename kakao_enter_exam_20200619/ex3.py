from collections import defaultdict


def segment(x, space):
    if x == 1:
        return max(space)
    memos = [defaultdict(int) for _ in range(x)]
    for i in range(len(space) - x + 1):
        seg = space[i:i + x]
        if i == 0:
            memos[x - 1][i] = seg[-1]
            for j in range(x - 2, -1, -1):
                memos[j][i] = min(memos[j + 1][i], seg[j])
            continue
        for j in range(x):
            if j == x - 1:
                memos[j][i] = space[i + x - 1]
                continue
            memos[j][i] = min(memos[j + 1][i - 1], space[i + x - 1])
    return max(memos[0].values())


if __name__ == '__main__':
    x = 3
    space = [2, 5, 4, 6, 8]
    result = segment(x, space)
    print(result)
