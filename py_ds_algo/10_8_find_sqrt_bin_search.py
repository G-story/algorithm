def find_sqrt_bin_search(n, error=0.001):
    min, max = 1, n
    sqrt = (min + max) / 2
    while abs(n - sqrt ** 2) > error:
        if sqrt ** 2 < n:
            min, sqrt = sqrt, (sqrt + max) / 2
        else:
            max, sqrt = sqrt, (sqrt + min) / 2
    return sqrt


if __name__ == "__main__":
    a = 2
    b = 9
    import math

    print(math.sqrt(a))
    print(find_sqrt_bin_search(a))
    print(math.sqrt(b))
    print(find_sqrt_bin_search(b))
