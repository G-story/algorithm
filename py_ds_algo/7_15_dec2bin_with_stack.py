from stack import Stack


def dec2bin_with_stack(decnum):
    st = Stack()
    n = decnum
    while n >= 1:
        st.push(n % 2)
        n = n // 2
    bin_str = ''
    while not st.is_empty():
        bin_str += str(st.pop())
    return bin_str


if __name__ == "__main__":
    decnum = 9
    print(dec2bin_with_stack(decnum))
