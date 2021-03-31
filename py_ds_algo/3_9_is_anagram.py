from collections import Counter


def is_anagram(s1, s2):
    return len(Counter(s1) - Counter(s2)) == 0


def test_is_anagram():
    s1 = "marina"
    s2 = "aniram"
    assert (is_anagram(s1, s2) is True)
    s1 = "google"
    s2 = "gouglo"
    assert (is_anagram(s1, s2) is False)
    print("테스트 통과!")


if __name__ == "__main__":
    test_is_anagram()
