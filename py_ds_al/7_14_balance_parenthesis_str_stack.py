from stack import Stack


def balance_par_str_with_stack(str1):
    st = Stack()
    for c in str1:
        if c == '(':
            st.push(c)
        elif c == ')':
            if st.is_empty():
                return False
            st.pop()
    return st.is_empty()


if __name__ == "__main__":
    print(balance_par_str_with_stack('((()))'))
    print(balance_par_str_with_stack('(()'))
