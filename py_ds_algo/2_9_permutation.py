from itertools import permutations, combinations


def perm(s):
    if len(s) == 1:
        return [s]
    result = []
    for x in perm(s[1:]):
        for i in range(len(x) + 1):
            result.append(x[:i] + s[0] + x[i:])
    return result


def perm2(s):
    return [''.join(x) for x in permutations(s)]


def combination(s):
    return [''.join(x) for x in combinations(val, 2)]


if __name__ == "__main__":
    val = "012"
    print(perm(val))
    print(perm2(val))
    print(combination(val))
