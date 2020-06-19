def finding_gcd(a, b):
    divisors = []
    gcd = 1
    for i in range(2, min(a, b)):
        while a % i == 0 or b % i == 0:
            if a % i == 0 and b % i == 0:
                a, b = a // i, b // i
                gcd *= i
                divisors.append(i)
            elif a % i == 0:
                a //= i
            elif b % i == 0:
                b //= i
    return gcd


def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert (finding_gcd(number1, number2) == 3)
    print("테스트 통과!")


if __name__ == '__main__':
    test_finding_gcd()
