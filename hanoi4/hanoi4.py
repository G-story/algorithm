class Hanoi4(object):
    def __init__(self, disks):
        self.disks = disks

    def get_move_cnt(self):
        pass


def get_result():
    N = int(input())
    disks = []
    for i in range(4):
        inp = input().split()
        disks.append(map(int, inp[1:]))
    return Hanoi4(disks).get_move_cnt()


if __name__ == '__main__':
    C = input()
    for i in range(C):
        print get_result()
