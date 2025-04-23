import pygame
from sympy.codegen.ast import continue_

from move_validator import MoveValidator
from constants import *


class Frontend:
    def __init__(self, board,difficulty, mode):
        self.board = board
        self.difficulty = difficulty
        self.mode = mode
        self.mv = MoveValidator(board.p1_pawns_fields, board.p2_pawns_fields)
        self.selected = None
        self.possible_moves = None
        self.current_player = 0
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

            self.possible_moves = self.mv.pawn_possible_moves(x, y)
            for a,b in self.possible_moves:
                rect = pygame.Rect(a * TILE_SIZE, b * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.screen, GREEN, rect, 3)

        pygame.display.flip()

    def handle_click(self, pos, player_pawns):
        x, y = pos[0] // TILE_SIZE, pos[1] // TILE_SIZE
        print("X: {x}  Y: {y}".format(x=x, y=y))
        if self.selected:
            if (x,y) in self.possible_moves:
                self.board.move_pawn(self.selected[0], self.selected[1], x, y)
                if self.mode == "PvP":
                    self.current_player = (self.current_player + 1) % 2
                elif self.mode == "PvE":
                    a = 1
                self.selected = None
                self.possible_moves = None
            else:
                self.selected = None
                self.possible_moves = None
        else:
            if (x,y) in player_pawns:
                self.selected = (x, y)

