import csv
import pygame
import sys
#pobranie struktury przycisku ze skryptu button
from button import Button

#deklaracja rozmiarów okna
SCREEN = pygame.display.set_mode((1280, 720))
#zczytanie zmiennych z assetów
BG_MENU = pygame.image.load("assets/menu.png")

#Deklaracja czcionki i jej rozmiaru
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def values():
    pygame.display.set_caption("Options")

    while True:
        # Wgranie zdjęcia i zczytanie pozycji kursora.
        SCREEN.blit(BG_MENU, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()

        MENU_TITLE = get_font(100).render("SELECT OPTIONS", True, "#68228B")
        MENU_RECT = MENU_TITLE.get_rect(center=(640, 100))

        # wyrenderowanie napisu Menu na stronie głównej i podanie jego pozycji.
        SCREEN.blit(MENU_TITLE, MENU_RECT)

        pygame.display.update()