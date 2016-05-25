import math


class Arctic:
    def __init__(self):
        pass

    @classmethod
    def get_min_elec_dist(cls, bases):
        lines = [[10000 for j in xrange(100)] for i in xrange(100)]

        for i, xy in enumerate(bases):
            for j in range(i + 1, len(bases)):
                lines[i][j] = round(math.sqrt((xy[0] - bases[j][0]) ** 2 + (xy[1] - bases[j][1]) ** 2), 2)

        for ls in lines:
            pass


if __name__ == '__main__':
    c = int(raw_input())
    for i in xrange(c):
        n = int(raw_input())
        print Arctic.get_min_elec_dist([[float(j) for j in raw_input().split()] for i in n])
