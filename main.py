import pygame
import sys
#pobranie struktury przycisku ze skryptu button
from button import Button

import options_game
import car as symulation

pygame.init()

#Podanie wymiarów
SCREEN = pygame.display.set_mode((1280, 720))

#zczytanie zmiennych z assetów
BG_MENU = pygame.image.load("assets/menu.png")

#Deklaracja czcionki i jej rozmiaru
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    symulation.play()
    main_menu()

    pygame.display.update()

def options():
    options_game.values()
    main_menu()

    pygame.display.update()

def main_menu():
    #nazwanie okan startowego
    pygame.display.set_caption("Menu")

    while True:
        #Wgranie zdjęcia i zczytanie pozycji kursora.
        SCREEN.blit(BG_MENU, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()
        #wyrenderowanie napisu Menu na stronie głównej i podanie jego pozycji.
        MENU_TITLE = get_font(100).render("MENU", True, "#68228B")
        MENU_RECT = MENU_TITLE.get_rect(center=(640, 100))

        #Deklaracja przycisków, stylu, rozmiaru, wyglądu, pozycji
        PLAY_BUTTON = Button(image=pygame.image.load("assets/bg_play_button.png"),
                             pos=(640, 250),
                             text_input="PLAY",
                             font=get_font(75),
                             base_color="#68228B",
                             hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/bg_options_button.png"),
                             pos=(640, 400),
                             text_input="OPTIONS",
                             font=get_font(75),
                             base_color="#68228B",
                             hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/bg_quit_button.png"),
                             pos=(640, 550),
                             text_input="QUIT",
                             font=get_font(75),
                             base_color="#68228B",
                             hovering_color="White")

        # wyrenderowanie napisu Menu na stronie głównej i podanie jego pozycji.
        SCREEN.blit(MENU_TITLE, MENU_RECT)

        #Funkcja która zienaia nam kolor po najechaniu na danyc przycisk
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        #dodanie finkcji przyciskom + funkcji wychodzenia poprzez zamknięcie okienka
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()