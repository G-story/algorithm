from enum import Enum


class Spliter:
    pieces = []


class PieceType(Enum):
    repeated_nums = 1
    sequential = 2
    zigzag = 4
    equal_diff = 5
    other = 10


class PieceManager:
    type = PieceType.other
    nums = []


def execute(func):
    n = int(input())

    for i in range(n):
        print(func())


def temp():
    n_piece_set = int(input())
    return "hi"


execute(temp)
