def get_max_past_and_future(a, b, d):
    return []


def in_out():
    inp = input().split()
    V = int(inp[0])
    W = int(inp[1])
    a, b, d = [], [], []
    for i in range(W):
        inp = input().split()
        a.append(int(inp[0]))
        b.append(int(inp[1]))
        d.append(int(inp[2]))
    result = get_max_past_and_future(a, b, d)
    print(result)


if __name__ == '__main__':
    C = int(input())
    for i in range(C):
        in_out()
