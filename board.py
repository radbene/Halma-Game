from typing import Optional, Tuple, Set

from pawn import Pawn

class Board():
    def __init__(self,p1_sign: str, p2_sign: str):
        self.size: int = 16
        self.fields = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.p1_fields: set[tuple[int, int]] = set()
        self.p2_fields: set[tuple[int, int]] = set()
        #self.fields[6][1] = Pawn(6, 1, "X")
        for i in range(5):
            j: int = min(5,6 - i)
            for k in range(j):
                self.fields[i][k] = Pawn(i, j, p1_sign)
                self.fields[self.size - i - 1][self.size - k - 1] = Pawn(self.size - i - 1, self.size - j - 1, p2_sign)
                self.p1_fields.add((i,k))
                self.p2_fields.add((self.size - i - 1, self.size - k - 1))
        self.p1_pawns_fields: set[tuple[int, int]] = self.p1_fields.copy()
        self.p2_pawns_fields: set[tuple[int, int]] = self.p2_fields.copy()

    def move_pawn(self,curr_x, curr_y, new_x, new_y):
        if (curr_x, curr_y) in self.p1_pawns_fields:
            self.p1_pawns_fields.remove((curr_x, curr_y))
            self.p1_pawns_fields.add((new_x, new_y))
        elif (curr_x, curr_y) in self.p2_pawns_fields:
            self.p2_pawns_fields.remove((curr_x, curr_y))
            self.p2_pawns_fields.add((new_x, new_y))



    def get_pawn(self, i: int, j: int) -> str:
        if isinstance(self.fields[i][j], Pawn):
            return self.fields[i][j].player
        return "0"

    def get_occupied_fields(self) -> set[tuple[int, int]]:
        return self.p1_pawns_fields | self.p2_pawns_fields

    def __str__(self):
        representation = ""
        for row in self.fields:
            for cell in row:
                representation += str(cell) + " "
            representation += "\size"
        return representation
