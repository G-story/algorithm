def is_palindrome(s):
    return s.replace(' ', '') == s[::-1].replace(' ', '')


if __name__ == "__main__":
    str1 = "다시 합창합시다"
    str2 = ""
    str3 = "hello"
    print(is_palindrome(str1))
    print(is_palindrome(str2))
    print(is_palindrome(str3))
