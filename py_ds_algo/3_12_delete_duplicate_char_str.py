from collections import Counter


def delete_unique_word(str1):
    result = ''
    for c in str1:
        if Counter(str1)[c] > 1:
            continue
        result += c
    return result


def test_delete_unique_word():
    str1 = "google"
    assert (delete_unique_word(str1) == "le")
    print("테스트 통과!")


if __name__ == "__main__":
    test_delete_unique_word()
