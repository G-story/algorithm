class Lunchbox:
    def __init__(self):
        pass

    @classmethod
    def get_fast_time(cls, m_list, e_list):
        if len(m_list) == 0 or len(e_list) == 0:
            return
        max_time = 0
        while len(m_list) > 0:
            min_e_idx, min_e = min(enumerate(e_list), key=lambda p: p[1])
            max_time = max(max_time, sum(m_list) + min_e)
            del m_list[min_e_idx]
            del e_list[min_e_idx]

        return max_time


if __name__ == '__main__':
    c = int(raw_input())
    for i in xrange(c):
        n = int(raw_input())
        print Lunchbox.get_fast_time([int(inp) for inp in raw_input().split()],
                                     [int(inp) for inp in raw_input().split()])
