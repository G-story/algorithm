from collections import deque


def requestsServed(timestamp, top):
    d = deque()
    count = 0
    timestamp = deque(sorted(timestamp))
    top = deque(sorted(top))
    for sec in range(60):
        if not top:
            break
        while timestamp and timestamp[0] == sec:
            d.append(timestamp.popleft())
        while top and top[0] == sec:
            for _ in range(5):
                if d:
                    d.pop()
                    count += 1
                else:
                    break
            top.popleft()
    return count


if __name__ == '__main__':
    timestamp = [0, 0] + 15 * [1]
    top = [6, 6, 6, 6]
    result = requestsServed(timestamp, top)
    print(result)
