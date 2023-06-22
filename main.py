import pygame
import sys
#pobranie struktury przycisku ze skryptu button
from button import Button

import csv

import car as symulation

csv_data = './dane.csv'

pygame.init()

#Podanie wymiarów
SCREEN = pygame.display.set_mode((1280, 720))

#zczytanie zmiennych z assetów
BG_MENU = pygame.image.load("assets/menu.png")

#Deklaracja czcionki i jej rozmiaru
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def values():
    pygame.display.set_caption("Options")

    mapa = ""
    pojazd = ""
    licz = 0
    czas = 0
    pre = 0
    gene = 0

    #Wczytanie danychz pliku CSV
    with open(csv_data, 'r') as plik_csv:
        czytnik = csv.DictReader(plik_csv)
        for wiersz in czytnik:
            mapa = wiersz['mapa']
            pojazd = wiersz['pojazd']
            licz = int(wiersz['licz'])
            czas = int(wiersz['czas'])
            pre = int(wiersz['pre'])
            gene = int(wiersz['gene'])
            break

    print("Wczytane wartości:")
    print("mapa:", mapa)
    print("pojazd:", pojazd)
    print("licz:", licz)
    print("czas:", czas)
    print("pre:", pre)
    print("gene:", gene)

    while True:
        # Wgranie zdjęcia i zczytanie pozycji kursora.
        SCREEN.blit(BG_MENU, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()

        MENU_TITLE = get_font(60).render("SELECT OPTIONS", True, "#68228B")
        MENU_RECT = MENU_TITLE.get_rect(center=(640, 100))

        #wyrenderowanie napisu Menu na stronie głównej i podanie jego pozycji.
        SCREEN.blit(MENU_TITLE, MENU_RECT)

        OPTIONS_TEXT = get_font(20).render("Wybierz poziom trudności mapy:", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 180))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        EASY = Button(image=None,
                      pos=(340, 210),
                      text_input="EASY",
                      font=get_font(20),
                      base_color="#68228B",
                      hovering_color="White")

        MEDIUM = Button(image=None,
                        pos=(640, 210),
                        text_input="MEDIUM",
                        font=get_font(20),
                        base_color="#68228B",
                        hovering_color="White")

        HARD = Button(image=None,
                      pos=(940, 210),
                      text_input="HARD",
                      font=get_font(20),
                      base_color="#68228B",
                      hovering_color="White")

        OPTIONS_TEXT = get_font(20).render("Wybierz kolor samochodu:", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 240))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        PINK_CAR = Button(image=None,
                          pos=(340, 270),
                          text_input="PINK",
                          font=get_font(20),
                          base_color="#68228B",
                          hovering_color="White")

        YELLOW_CAR = Button(image=None,
                            pos=(640, 270),
                            text_input="YELLOW",
                            font=get_font(20),
                            base_color="#68228B",
                            hovering_color="White")

        GREEN_CAR = Button(image=None,
                           pos=(940, 270),
                           text_input="GREEN",
                           font=get_font(20),
                           base_color="#68228B",
                           hovering_color="White")

        OPTIONS_TEXT = get_font(20).render("PODAJ LICZEBNOSC POPULACJI Z JAKĄ CHCESZ SYMULOWAC:", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 300))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        LICZEBNOŚC_LESS = Button(image=None,
                           pos=(500, 350),
                           text_input="<",
                           font=get_font(20),
                           base_color="#68228B",
                           hovering_color="White")

        LICZEBNOŚC_INFO = get_font(20).render(str(licz), True, "Black")
        LICZEBNOŚC_INFO_RECT = OPTIONS_TEXT.get_rect(center=(1150, 350))
        SCREEN.blit(LICZEBNOŚC_INFO, LICZEBNOŚC_INFO_RECT)



        LICZEBNOŚC_MORE = Button(image=None,
                      pos=(800, 350),
                      text_input=">",
                      font=get_font(20),
                      base_color="#68228B",
                      hovering_color="White")

        OPTIONS_TEXT = get_font(20).render("PODAJ CZAS KAZDEJ SYMULACJI (DOMYSLNA 12s):", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 400))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        CZAS_LESS = Button(image=None,
                                      pos=(500, 450),
                                      text_input="<",
                                      font=get_font(20),
                                      base_color="#68228B",
                                      hovering_color="White")

        CZAS_INFO = get_font(20).render(str(czas), True, "Black")
        CZAS_INFO_RECT = OPTIONS_TEXT.get_rect(center=(1070, 450))
        SCREEN.blit(CZAS_INFO, CZAS_INFO_RECT)

        CZAS_MORE = Button(image=None,
                                 pos=(800, 450),
                                 text_input=">",
                                 font=get_font(20),
                                 base_color="#68228B",
                                 hovering_color="White")

        OPTIONS_TEXT = get_font(20).render("PODAJ PREDKOSC STARTOWA (ZALECANA 20 - DOMYSLNA):", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 500))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        SPEED_LESS = Button(image=None,
                           pos=(500, 550),
                           text_input="<",
                           font=get_font(20),
                           base_color="#68228B",
                           hovering_color="White")

        SPEED_INFO = get_font(20).render(str(pre), True, "Black")
        SPEED_INFO_RECT = OPTIONS_TEXT.get_rect(center=(1130, 550))
        SCREEN.blit(SPEED_INFO, SPEED_INFO_RECT)

        SPEED_MORE = Button(image=None,
                           pos=(800, 550),
                           text_input=">",
                           font=get_font(20),
                           base_color="#68228B",
                           hovering_color="White")

        OPTIONS_TEXT = get_font(20).render("PODAJ ILOŚĆ POPULACJI:", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 600))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        POPULACJE_LESS = Button(image=None,
                                 pos=(500, 650),
                                 text_input="<",
                                 font=get_font(20),
                                 base_color="#68228B",
                                 hovering_color="White")

        POPULACJE_INFO = get_font(20).render(str(gene), True, "Black")
        POPULACJE_INFO_RECT = OPTIONS_TEXT.get_rect(center=(860, 650))
        SCREEN.blit(POPULACJE_INFO, POPULACJE_INFO_RECT)

        POPULACJE_MORE = Button(image=None,
                                 pos=(800, 650),
                                 text_input=">",
                                 font=get_font(20),
                                 base_color="#68228B",
                                 hovering_color="White")

        # przyciks cofania do menu
        BACK = Button(image=None,
                      pos=(640, 690),
                      text_input="BACK",
                      font=get_font(45),
                      base_color="#68228B",
                      hovering_color="White")


        for button in [EASY, MEDIUM, HARD, PINK_CAR, YELLOW_CAR, GREEN_CAR, LICZEBNOŚC_LESS, LICZEBNOŚC_MORE, CZAS_LESS, CZAS_MORE, SPEED_LESS, SPEED_MORE, POPULACJE_LESS, POPULACJE_MORE]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)


        BACK.changeColor(MOUSE_POS)
        BACK.update(SCREEN)


        #funkcje przycisków
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(MOUSE_POS):
                    #wczytanie zmiennych do pliku csv
                    with open(csv_data, 'w', newline='') as plik_csv:
                        writer = csv.writer(plik_csv)
                        writer.writerow(['mapa', 'pojazd', 'licz', 'czas', 'pre', 'gene'])
                        writer.writerow([mapa, pojazd, licz, czas, pre, gene])
                    main_menu()
                #Edycja danych
                if EASY.checkForInput(MOUSE_POS):
                    mapa = "map_easy"
                if MEDIUM.checkForInput(MOUSE_POS):
                    mapa = "map_basic"
                if HARD.checkForInput(MOUSE_POS):
                    mapa = "map_basic"
                if PINK_CAR.checkForInput(MOUSE_POS):
                    pojazd = "car_p"
                if YELLOW_CAR.checkForInput(MOUSE_POS):
                    pojazd = "car_y"
                if GREEN_CAR.checkForInput(MOUSE_POS):
                    pojazd = "car_g"
                if LICZEBNOŚC_LESS.checkForInput(MOUSE_POS):
                    licz = licz - 5
                    LICZEBNOŚC_INFO = get_font(20).render(str(licz), True, "Black")
                    LICZEBNOŚC_INFO_RECT = OPTIONS_TEXT.get_rect(center=(1150, 350))
                    SCREEN.blit(LICZEBNOŚC_INFO, LICZEBNOŚC_INFO_RECT)
                if LICZEBNOŚC_MORE.checkForInput(MOUSE_POS):
                    licz = licz + 5
                    LICZEBNOŚC_INFO = get_font(20).render(str(licz), True, "Black")
                    LICZEBNOŚC_INFO_RECT = OPTIONS_TEXT.get_rect(center=(1150, 350))
                    SCREEN.blit(LICZEBNOŚC_INFO, LICZEBNOŚC_INFO_RECT)
                if CZAS_LESS.checkForInput(MOUSE_POS):
                    czas = czas - 5
                    CZAS_INFO = get_font(20).render(str(czas), True, "Black")
                    CZAS_INFO_RECT = OPTIONS_TEXT.get_rect(center=(1070, 450))
                    SCREEN.blit(CZAS_INFO, CZAS_INFO_RECT)
                if CZAS_MORE.checkForInput(MOUSE_POS):
                    czas = czas + 5
                    CZAS_INFO = get_font(20).render(str(czas), True, "Black")
                    CZAS_INFO_RECT = OPTIONS_TEXT.get_rect(center=(1070, 450))
                    SCREEN.blit(CZAS_INFO, CZAS_INFO_RECT)
                if SPEED_LESS.checkForInput(MOUSE_POS):
                    pre = pre - 5
                    SPEED_INFO = get_font(20).render(str(pre), True, "Black")
                    SPEED_INFO_RECT = OPTIONS_TEXT.get_rect(center=(1130, 550))
                    SCREEN.blit(SPEED_INFO, SPEED_INFO_RECT)
                if SPEED_MORE.checkForInput(MOUSE_POS):
                    pre = pre + 5
                    SPEED_INFO = get_font(20).render(str(pre), True, "Black")
                    SPEED_INFO_RECT = OPTIONS_TEXT.get_rect(center=(1130, 550))
                    SCREEN.blit(SPEED_INFO, SPEED_INFO_RECT)
                if POPULACJE_LESS.checkForInput(MOUSE_POS):
                    gene = gene - 5
                    POPULACJE_INFO = get_font(20).render(str(gene), True, "Black")
                    POPULACJE_INFO_RECT = OPTIONS_TEXT.get_rect(center=(860, 650))
                    SCREEN.blit(POPULACJE_INFO, POPULACJE_INFO_RECT)
                if POPULACJE_MORE.checkForInput(MOUSE_POS):
                    gene = gene + 5
                    POPULACJE_INFO = get_font(20).render(str(gene), True, "Black")
                    POPULACJE_INFO_RECT = OPTIONS_TEXT.get_rect(center=(860, 650))
                    SCREEN.blit(POPULACJE_INFO, POPULACJE_INFO_RECT)




        pygame.display.update()

def play():
    symulation.play()
    main_menu()

    pygame.display.update()

def options():
    values()

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