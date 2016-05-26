class Josephus(object):
    @classmethod
    def get_two_person(cls, n, k):
        people = range(1, n + 1)
        i = 0
        while len(people) > 2:
            del people[i]
            i += k - 1
            i %= len(people)
        return people[0], people[1]


if __name__ == '__main__':
    c = int(raw_input())
    for i in xrange(c):
        print ' '.join([str(p) for p in Josephus.get_two_person(*(tuple(int(inp) for inp in raw_input().split())))])
