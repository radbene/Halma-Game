import board
from frontend import Frontend
import pygame
from game_modes import GameMode
from menu import show_menu

class Game():
    def __init__(self,p1_sign: str, p2_sign: str):
        self.board = board.Board(p1_sign, p2_sign)
        self.game_on: bool = True
        self.difficulty: str = "Easy"

    def start_game(self):
        difficulty,mode = show_menu()
        self.difficulty = difficulty
        frontend = Frontend(self.board,difficulty,mode)
        while self.game_on:
            frontend.draw_board()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_on = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mode == "PvP":
                        self.pvp_turn(frontend)
                    elif mode == "PvE":
                        self.pve_turn(frontend)
                    if self.check_win(self.board.p1_pawns_fields,self.board.p1_base):
                        print("Player 1 Won!")
                    elif self.check_win(self.board.p2_pawns_fields,self.board.p2_base):
                        print("Player 2 Won!")

    def pvp_turn(self,frontend):
        turns = [self.board.p1_pawns_fields, self.board.p2_pawns_fields]
        frontend.handle_click(pygame.mouse.get_pos(), turns[frontend.current_player])

    def pve_turn(self,frontend):
        #TODO: make a computer that makes moves based on a chosen difficulty
        pass

    def check_win(self, player_pawns: set[tuple[int,int]], player_base = set[tuple[int,int]]) -> bool:
        win: bool = True
        for position in player_pawns:
            if position in player_base:
                continue
            else:
                win = False
                break
        if win:
            self.game_on = False
        return win
