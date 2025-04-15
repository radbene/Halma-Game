import board
from frontend import Frontend
import pygame
from pawn import Pawn
from game_modes import GameMode
from menu import show_menu

class Game():
    def __init__(self,p1_sign: str, p2_sign: str):
        self.board = board.Board(p1_sign, p2_sign)
        self.game_on: bool = True

    def start_game(self):
        difficulty,mode = show_menu()
        turns = [self.board.p1_pawns_fields,self.board.p2_pawns_fields]
        turn_idx = 0
        frontend = Frontend(self.board)
        while self.game_on:
            frontend.draw_board()
            if turn_idx == 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_on = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        frontend.handle_click(pygame.mouse.get_pos(),turns[turn_idx])

            turn_idx = (turn_idx + 1) % len(turns)


    def check_win(self, player_pawns: set[Pawn], player_base = set[tuple[int,int]]) -> bool:
        win: bool = True
        for pawn in player_pawns:
            position = (pawn.row,pawn.col)
            if position in player_base:
                continue
            else:
                win = False
                break
        if win:
            self.game_on = False
        return win
