import math


class Arctic:
    def __init__(self):
        pass

    @classmethod
    def get_min_elec_dist(cls, bases):
        lines = []
        for i, from_xy in enumerate(bases):
            line = []
            for j, to_xy in enumerate(bases):
                line.append(round(math.sqrt((from_xy[0] - to_xy[0]) ** 2 + (from_xy[1] - to_xy[1]) ** 2), 2))
            lines.append(line)

        selected = len(bases) * [False]
        selected[0] = True
        seleted_idxs = [0]
        selected_lines = []
        for i in xrange(len(bases) - 1):
            min_idx, min_dist = 0, 1000
            for j in seleted_idxs:
                for k, l in enumerate(lines[j]):
                    if selected[k] == False and l < min_dist:
                        min_idx, min_dist = k, l
            selected[min_idx] = True
            seleted_idxs.append(min_idx)
            selected_lines.append(min_dist)

        return max(selected_lines)


if __name__ == '__main__':
    c = int(raw_input())
    for i in xrange(c):
        n = int(raw_input())
        print Arctic.get_min_elec_dist([[float(j) for j in raw_input().split()] for i in xrange(n)])
