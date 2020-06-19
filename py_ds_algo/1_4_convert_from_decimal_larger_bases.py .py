def convert_from_decimal_larger_bases(number, base):
    a = number
    result = ''
    while a >= 1:
        a, b = divmod(a, base)
        result += str(b) if b < 10 else chr(b + 54)
    return int(result[::-1])


def test_convert_from_decimal_larger_bases():
    number, base = 31, 16
    assert(convert_from_decimal_larger_bases(number, base) == "1F")
    print("테스트 통과!")


if __name__ == '__main__':
    test_convert_from_decimal_larger_bases()
