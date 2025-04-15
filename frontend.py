import pygame
from move_validator import MoveValidator

TILE_SIZE = 40
PADDING = 4
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Frontend:
    def __init__(self, board):
        self.board = board
        self.mv = MoveValidator(board)
        self.selected = None
        self.possible_moves = None
        self.current_player = 1
        self.screen = pygame.display.set_mode((board.size * TILE_SIZE, board.size * TILE_SIZE))

    def draw_board(self):
        self.screen.fill(WHITE)
        for y in range(self.board.size):
            for x in range(self.board.size):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.screen, GRAY, rect, 1)

        for p in self.board.p1_pawns_fields:
            x,y = p
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.circle(self.screen, BLUE, rect.center, TILE_SIZE // 2 - 4)

        for p in self.board.p2_pawns_fields:
            x,y = p
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.circle(self.screen, RED, rect.center, TILE_SIZE // 2 - 4)

        if self.selected:
            x, y = self.selected
            sel_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(self.screen, RED, sel_rect, 3)

            self.possible_moves = self.mv.can_move(x,y)
            for a,b in self.possible_moves:
                rect = pygame.Rect(a * TILE_SIZE, b * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.screen, GREEN, rect, 3)

        pygame.display.flip()

    def handle_click(self, pos, player_pawns):
        x, y = pos[0] // TILE_SIZE, pos[1] // TILE_SIZE
        if self.selected:
            if (x,y) in self.possible_moves:
                self.board.move_pawn(self.selected[0], self.selected[1], x, y)
                self.current_player = 2 if self.current_player == 1 else 1
                self.selected = None
                self.possible_moves = None
            else:
                self.selected = None
                self.possible_moves = None
        else:
            if (x,y) in player_pawns:
                self.selected = (x, y)

