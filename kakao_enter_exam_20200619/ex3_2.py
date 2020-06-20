import heapq
import time
from random import randint


def segment(x, space):
    result = 0
    arr = []
    h = []
    for v in space:
        if len(h) == x:
            h.remove(arr[0])
            heapq.heapify(h)
            del arr[0]
        arr.append(v)
        heapq.heappush(h, v)
        if len(h) == x:
            result = max(result, h[0])
    return result


def segment2(x, space):
    result = 0
    for i in range(len(space) - x + 1):
        if space[i + x - 1] <= result:
            continue
        seg = space[i:i + x]
        result = max(result, min(seg))
    return result


def segment3(x, space):
    result = 0
    min_num = 0
    for i in range(len(space) - x + 1):
        if i > 0 and x > 2 and space[i - 1] != min_num:
            continue
        seg = space[i:i + x]
        min_num = min(seg)
        result = max(result, min_num)
    return result


if __name__ == '__main__':
    _x = 100
    _space = [randint(1, 1000000) for _ in range(1000000)]
    for func in [segment, segment2, segment3]:
        t0 = time.time()
        res = func(_x, _space)
        t1 = time.time()
        print(res)
        print(t1 - t0)
