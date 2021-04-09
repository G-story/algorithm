from math import ceil, gcd


def solution(w, h):
    def func(x):
        return (- (h / w)) * x + h

    limit = int(w / gcd(w, h))
    if w == h:
        return w * h - w
    elif w == 1 or h == 1:
        return 0
    return w * h - (gcd(w, h) * sum(ceil(ceil(func(x)) - func(x + 1)) for x in range(limit)))


if __name__ == '__main__':
    print(solution(12, 8))
