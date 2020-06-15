from collections import deque


def palindrome_checker_with_deque(str1):
    deq = deque()

    for c in str1.lower():
        if not c.strip():
            continue
        deq.append(c)

    while len(deq) >= 2:
        if deq.pop() != deq.popleft():
            return False
    return True


if __name__ == "__main__":
    str1 = "Madam Im Adam"
    str2 = "Buffy is a Slayer"
    print(palindrome_checker_with_deque(str1))
    print(palindrome_checker_with_deque(str2))
