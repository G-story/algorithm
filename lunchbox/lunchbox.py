class Lunchbox:
    def __init__(self):
        pass

    @classmethod
    def get_fast_time(cls, m_list, e_list):
        sorted_list = sorted(zip(m_list, e_list), key=lambda a: a[1], reverse=True)
        stacked_sum_m = 0
        max_time = 0
        for item in sorted_list:
            stacked_sum_m += item[0]
            finish_time = stacked_sum_m + item[1]
            max_time = finish_time if finish_time > max_time else max_time

        return max_time


if __name__ == '__main__':
    c = int(raw_input())
    for i in xrange(c):
        n = int(raw_input())
        print Lunchbox.get_fast_time([int(inp) for inp in raw_input().split()],
                                     [int(inp) for inp in raw_input().split()])
