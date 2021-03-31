class Numbergame:
    nums = None
    cache = None

    @classmethod
    def numbergame(cls, start, end):
        nums = cls.nums
        numbergame = cls.numbergame
        cache = cls.cache
        if end - start <= 0:
            return 0
        if end - start == 1:
            return nums[start]
        if cache[start][end - 1] != 1111:
            return cache[start][end - 1]
        result = [nums[start] - numbergame(start + 1, end), nums[end - 1] - numbergame(start, end - 1)]
        if end - start >= 2:
            result += [-numbergame(start + 2, end), -numbergame(start, end - 2)]
        ret = max(result)
        cache[start][end - 1] = ret
        return ret

    @classmethod
    def work(cls, nums):
        cls.nums = nums
        cls.cache = [[1111 for i in xrange(50)] for j in xrange(50)]
        ret = cls.numbergame(0, len(nums))
        return ret


if __name__ == '__main__':
    c = int(raw_input())
    for i in xrange(c):
        n = int(raw_input())
        print Numbergame.work([int(inp) for inp in raw_input().split()])
