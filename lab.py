def segmentsUnion(left, right):
    answer = 0
    events = []
    opened = 0

    for i in range(len(left)):
        events.append([left[i], 1])
        events.append([right[i], -1])

    events.sort()

    for i in range(len(events)):
        if opened > 0:
            answer += events[i][0] - events[i - 1][0]
        opened += events[i][1]

    return answer


print segmentsUnion([1, 2, 5], [3, 4, 6])
