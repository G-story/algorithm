class Piece(object):
    bb = "BB"

    def __init__(self, aa="abcd"):
        self.aa = aa


print(getattr(Piece(), "aa"))
