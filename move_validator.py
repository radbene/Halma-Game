from constants import *
class MoveValidator():
    def __init__(self, pawns: set[tuple[int, int]], opponent_pawns: set[tuple[int, int]]):
        self.pawns = pawns
        self.opponent_pawns = opponent_pawns

    def get_all_moves(self,is_first_player: bool):
        if is_first_player:
            moves = {pawn: self.pawn_possible_moves(*pawn) for pawn in self.pawns}
        else:
            moves = {pawn:self.pawn_possible_moves(*pawn) for pawn in self.opponent_pawns}

        return moves


    def get_occupied_fields(self) -> set[tuple[int, int]]:
        return self.pawns | self.opponent_pawns

    def field_is_free(self, i: int, j: int):
        occupied = self.get_occupied_fields()
        return not (i,j) in occupied

    def field_is_in_bounds(self, i: int, j: int):
        if i < 0 or i >= BOARD_SIZE or j < 0 or j >= BOARD_SIZE:
            return False
        return True

    def pawn_possible_moves(self, i: int, j: int):
        if self.field_is_free(i, j):
            print("This field is not a Pawn!")
            return []
        legal_moves: list[tuple[int, int]] = []
        jumps: list[tuple[int, int], tuple[int, int]] = []
        directions = [(a,b) for a in range(-1,2) for b in range(-1,2)]
        for dir in directions:
            a: int = i + dir[0]
            b: int = j + dir[1]
            x: int = a + dir[0]
            y: int = b + dir[1]
            if self.field_is_in_bounds(a,b) and self.field_is_free(a,b):
                legal_moves.append((a,b))
            elif self.field_is_in_bounds(a, b) and self.field_is_in_bounds(x,y) and self.field_is_free(x,y): #occupied by pawn
                legal_moves.append((x, y))
                jumps.append([(x,y),dir])

        while jumps:
            pos,d = jumps.pop()
            i: int = pos[0]
            j: int = pos[1]
            directions = [(a, b) for a in range(-1, 2) for b in range(-1, 2)]
            for dir in directions:
                if d[0] == -dir[0] and d[1] == -dir[1]: #cant move to current location
                    continue
                a: int = i + dir[0]
                b: int = j + dir[1]
                x: int = a + dir[0]
                y: int = b + dir[1]
                if self.field_is_in_bounds(a, b) and not self.field_is_free(a, b) and self.field_is_in_bounds(x, y) and self.field_is_free(x, y):  # occupied by pawn
                    legal_moves.append((x,y))
                    jumps.append([(x, y), dir])

        return legal_moves[::-1]    #sorted from furthest to closest