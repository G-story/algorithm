class Piece(object):
    bb = "BB"

    def __init__(self, aa="abcd"):
        self.aa = aa


a = [0, 2, 3]
b = ''.join(map(str, a))
print(b)
