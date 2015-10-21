class Piece(object):
    bb = "BB"

    def __init__(self, aa="abcd"):
        self.aa = aa

    def test(self):
        print(self.bb)


a = [Piece("aaa"), Piece("bbb"), Piece("ccc")]
p = Piece("aaa")
p2 = Piece("aaa")
print(Piece.bb, Piece().aa)
f = staticmethod
