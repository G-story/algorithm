from stack import Stack


def reverse_string_with_stack(str1):
    st = Stack()
    for c in str1:
        st.push(c)
    rev_str = ''
    while not st.is_empty():
        rev_str += st.pop()
    return rev_str


if __name__ == '__main__':
    str1 = '문자열 거꾸로 뒤집기'
    print(str1)
    print(reverse_string_with_stack(str1))
