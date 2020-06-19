def convert_to_decimal(number, base):
    n = 0
    for i, char in enumerate(str(number)[::-1]):
        n += (base ** i) * int(char)
    return n


def test_convert_to_decimal():
    number, base = 1001, 2
    assert (convert_to_decimal(number, base) == 9)
    print("테스트 통과!")


if __name__ == '__main__':
    test_convert_to_decimal(10111, 2)
