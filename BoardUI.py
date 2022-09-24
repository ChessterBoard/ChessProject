import sys
import pygame
from settings import Settings
from ChessPieces import WhiteQueen
import functions as gf


def run_game():
    pygame.init()
    cb_settings = Settings()
    screen = pygame.display.set_mode((cb_settings.screen_width, cb_settings.screen_height))
    pygame.display.set_caption("ChessBoard")
    queen = WhiteQueen(screen)

    while True:
        gf.check_events()
        gf.update_screen(Settings,screen,queen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(cb_settings.bg_color)
        queen.blitme()

        pygame.display.flip()


run_game()
