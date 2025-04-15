class Pawn():
    def __init__(self, row: int, col: int, player: str):
        self.row: int = row
        self.col: int = col
        self.player: str = player

    def __str__(self):
        return self.player