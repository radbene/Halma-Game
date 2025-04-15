from typing import Optional

from pawn import Pawn

class Board():
    def __init__(self,p1_sign: str, p2_sign: str):
        self.n: int = 16
        self.fields = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.p1_fields: set[tuple[int, int]] = set()
        self.p2_fields: set[tuple[int, int]] = set()
        #self.fields[6][1] = Pawn(6, 1, "X")
        for i in range(5):
            j = min(5,6 - i)
            for k in range(j):
                self.fields[i][k] = Pawn(i, j, p1_sign)
                self.fields[self.n - i - 1][self.n - k - 1] = Pawn(self.n - i - 1, self.n - j - 1, p2_sign)
                self.p1_fields.add((i,k))
                self.p2_fields.add((self.n - i - 1, self.n - k - 1))
        self.p1_pawns: set[tuple[int, int]] = self.p1_fields.copy()
        self.p2_pawns: set[tuple[int, int]] = self.p2_fields.copy()

    def get_pawn(self, i: int, j: int) -> Optional[Pawn]:
        if isinstance(self.fields[i][j], Pawn):
            return self.fields[i][j]
        return None

    def __str__(self):
        representation = ""
        for row in self.fields:
            for cell in row:
                representation += str(cell) + " "
            representation += "\n"
        return representation
