from pawn import Pawn

class Board():
    def __init__(self):
        self.n = 16
        self.fields = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.p1_fields = set()
        self.p2_fields = set()
        self.fields[6][1] = Pawn(6, 1, "X")
        for i in range(5):
            j = min(5,6 - i)
            for k in range(j):
                self.fields[i][k] = Pawn(i, j, "X")
                self.fields[self.n - i - 1][self.n - k - 1] = Pawn(self.n - i - 1, self.n - j - 1, "Y")
                self.p1_fields.add((i,k))
                self.p2_fields.add((self.n - i - 1, self.n - k - 1))

    def field_is_free(self, i, j):
        return not isinstance(self.fields[i][j], Pawn)

    def field_is_in_bounds(self, i, j):
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            return False
        return True

    def can_move(self, i, j):
        if self.field_is_free(i, j):
            print("This field is not a Pawn!")
            return []
        legal_moves = []
        jumps = []
        directions = [(a,b) for a in range(-1,2) for b in range(-1,2)]
        for dir in directions:
            a = i + dir[0]
            b = j + dir[1]
            x = a + dir[0]
            y = b + dir[1]
            if self.field_is_in_bounds(a,b) and self.field_is_free(a,b):
                legal_moves.append((a,b))
            elif self.field_is_in_bounds(a, b) and self.field_is_in_bounds(x,y) and self.field_is_free(x,y): #occupied by pawn
                legal_moves.append((x, y))
                jumps.append([(x,y),dir])

        while jumps:
            pos,d = jumps.pop()
            i = pos[0]
            j = pos[1]
            directions = [(a, b) for a in range(-1, 2) for b in range(-1, 2)]
            for dir in directions:
                if d[0] == -dir[0] and d[1] == -dir[1]:
                    continue
                a = i + dir[0]
                b = j + dir[1]
                x = a + dir[0]
                y = b + dir[1]
                if self.field_is_in_bounds(a, b) and not self.field_is_free(a, b) and self.field_is_in_bounds(x, y) and self.field_is_free(x, y):  # occupied by pawn
                    legal_moves.append((x,y))
                    jumps.append([(x, y), dir])

        for pos in legal_moves:
            self.fields[pos[0]][pos[1]] = "1"
        return legal_moves



    def __str__(self):
        representation = ""
        for row in self.fields:
            for cell in row:
                representation += str(cell) + " "
            representation += "\n"
        return representation
