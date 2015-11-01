from enum import Enum


class Cutter:
    MIN_PIECE_LEN = 3
    MAX_PIECE_LEN = 5

    def __init__(self):
        self.pieces = []

    def cut(self, piece_set):
        self.pieces.append(Piece(piece_set[0:self.MIN_PIECE_LEN]))
        start = self.MIN_PIECE_LEN
        end = self.MAX_PIECE_LEN
        while start < len(piece_set):
            if start < len(piece_set) - self.MIN_PIECE_LEN - 2:
                new_num = piece_set[start]
                new_nums = piece_set[start:start + 3]
                if getattr(self.pieces[-1], "check_new_nums")(new_num, new_nums):
                    getattr(self.pieces[-1], "append_to_nums")(new_num)
                    start += 1
                    if start == end:
                        self.pieces.append(Piece(piece_set[start:start + self.MIN_PIECE_LEN]))
                        start += self.MIN_PIECE_LEN
                        end = start + 2
                else:
                    self.pieces.append(Piece(piece_set[start:start + self.MIN_PIECE_LEN]))
                    start += self.MIN_PIECE_LEN
                    end = start + 2
            else:
                self.pieces.append(Piece(piece_set[start:]))
                break

    def get_total_level(self):
        total_level = 0
        for i in self.pieces:
            total_level += getattr(i, "piece_type").value
        return total_level


class PieceType(Enum):
    repeated_nums = 1
    sequential = 2
    zigzag = 4
    equal_diff = 5
    other = 10


class Piece:
    def __init__(self, nums):
        self.piece_type = self.check_type(nums)
        self.nums = nums

    def append_to_nums(self, new_nums):
        if type(new_nums) == list:
            self.nums.extend(new_nums)
        else:
            self.nums.append(new_nums)

    def check_new_nums(self, new_num, new_nums):
        temp_nums = self.nums.copy()
        temp_nums.append(new_num)
        joined_type = self.check_type(temp_nums)
        new_type = self.check_type(new_nums)

        if joined_type == self.piece_type and joined_type.value <= new_type.value:
            return True
        else:
            return False

    @staticmethod
    def check_type(nums):
        check_list = [True] * 5

        first_num = nums[0]
        second_num = nums[1]
        seq_diff = 0
        num_diff = 0

        if second_num - first_num == 1:
            check_list[3] = False
            seq_diff = 1
        elif second_num - first_num == -1:
            check_list[3] = False
            seq_diff = -1
        else:
            check_list[1] = False
            num_diff = nums[1] - nums[0]

        for i in range(1, len(nums)):
            if nums[i] != first_num:
                check_list[0] = False
            if i != len(nums) - 1 and nums[i + 1] - nums[i] != seq_diff:
                check_list[1] = False
            if not ((i % 2 == 0 and nums[i] == first_num) or (i % 2 == 1 and nums[i] == second_num)):
                check_list[2] = False
            if check_list[3] and i != len(nums) - 1 and nums[i + 1] - nums[i] != num_diff:
                check_list[3] = False

        switcher = {
            0: PieceType.repeated_nums,
            1: PieceType.sequential,
            2: PieceType.zigzag,
            3: PieceType.equal_diff,
            4: PieceType.other
        }
        for i in range(len(check_list)):
            if check_list[i]:
                return switcher.get(i)


def execute(func):
    n = int(input())

    for i in range(n):
        print(func())


def temp():
    piece_set_str = input()
    piece_set = list(map(int, piece_set_str))
    cutter = Cutter()
    cutter.cut(piece_set)
    return cutter.get_total_level()


execute(temp)
