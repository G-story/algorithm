class Brackets2(object):
    @classmethod
    def get_is_correct(cls, brackets):
        stack = []
        bdic = {')': '(', '}': '{', ']': '['}
        for b in brackets:
            if b in bdic.values():
                stack.append(b)
            elif len(stack) == 0 or b not in bdic:
                return 'NO'
            elif stack.pop() != bdic[b]:
                return 'NO'
        return 'YES' if len(stack) == 0 else 'NO'


if __name__ == '__main__':
    c = int(raw_input())
    for i in xrange(c):
        print Brackets2.get_is_correct(raw_input())
