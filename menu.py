import pygame
from constants import *

pygame.init()

# Ustawienia okna
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wybór trybu gry")


# Font
font = pygame.font.SysFont(None, 36)

# Przycisk
class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.clicked = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False

def show_menu():

    modes = [
        Button("PvP", 50, 50, 150, 50),
        Button("PvE", 50, 120, 150, 50)
    ]

    difficulties = []

    selected_difficulty = None
    selected_mode = None

    running = True
    while running:
        screen.fill(WHITE)

        if selected_mode == "PvE":

            difficulties = [
                Button("Easy", 400, 50, 150, 50),
                Button("Medium", 400, 120, 150, 50),
                Button("Hard", 400, 190, 150, 50)
            ]

        elif selected_mode == "PvP":
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in difficulties:
                    if btn.check_click(pos):
                        selected_difficulty = btn.text
                for btn in modes:
                    if btn.check_click(pos):
                        selected_mode = btn.text

        for btn in difficulties:
            btn.color = DARK_GRAY if btn.text == selected_difficulty else GRAY
            btn.draw(screen)

        for btn in modes:
            btn.color = DARK_GRAY if btn.text == selected_mode else GRAY
            btn.draw(screen)

        # Jeśli oba wybrane, zapisz i zakończ
        if selected_difficulty and selected_mode:
            print("Ustawienia zapisane.")
            running = False


        pygame.display.flip()

    pygame.quit()
    return selected_difficulty, selected_mode
