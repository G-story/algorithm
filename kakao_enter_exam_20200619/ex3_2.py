import heapq


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


if __name__ == '__main__':
    x = 3
    space = [2, 5, 4, 6, 8]
    result = segment(x, space)
    print(result)
