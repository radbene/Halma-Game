class Pawn():
    def __init__(self, row, col, player):
        self.row = row
        self.col = col
        self.player = player

    def __str__(self):
        return self.player