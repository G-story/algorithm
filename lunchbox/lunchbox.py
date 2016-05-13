class Lunchbox:
    def __init__(self):
        pass

    @classmethod
    def get_fast_time(cls, m_list, e_list):
        m_plus_e_times = [m_list[i] + e_list[i] for i in xrange(len(m_list))]
        for i in xrange(len(m_list)):
            copied_m_list = m_list[:]


if __name__ == '__main__':
    c = int(raw_input())
    for i in xrange(c):
        n = int(raw_input())
        Lunchbox.get_fast_time([int(inp) for inp in raw_input().split()], [int(inp) for inp in raw_input().split()])
