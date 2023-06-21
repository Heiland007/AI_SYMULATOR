import math
import random
import sys
import csv

import neat
import pygame

# Stale
# WIDTH(szerokosc) = 1600
# HEIGHT(wysokosc) = 880

WIDTH = 1920
HEIGHT = 1080

CAR_SIZE_X = 60
CAR_SIZE_Y = 60

#Wyznaczenie koloru granicy/kolizji
BORDER_COLOR = (255, 255, 255, 255)

current_generation = 0  #Licznik generacji


class Car:

    def __init__(self):
        #Ladowanie ducha i jego rotacji
        self.sprite = pygame.image.load('assets/car.png').convert()  #przyspieszenie konwersji
        self.sprite = pygame.transform.scale(self.sprite, (CAR_SIZE_X, CAR_SIZE_Y))
        self.rotated_sprite = self.sprite

        self.position = [830, 920]  #Pozycja startowa 
        self.angle = 0
        self.speed = 0

        self.speed_set = False  #Flaga dla predkosci defaultowej
        self.center = [self.position[0] + CAR_SIZE_X / 2, self.position[1] + CAR_SIZE_Y / 2]  #Obliczanie srodka

        self.radars = []  #Lista dla radarow
        self.drawing_radars = []  #Pokazywanie radarow

        self.alive = True  #Sprawdzanie czy samochod jest "zywy" z funkcja boolowska 

        self.distance = 0  #Przejechana odleglosc
        self.time = 0  #Czas ktory minal

    def draw(self, screen):
        screen.blit(self.rotated_sprite, self.position)  #pokazujemy ducha
        self.draw_radar(screen)  #popkazujemy sensory

    def draw_radar(self, screen):
        #Pokazujemy wszystkie radary
        for radar in self.radars:
            position = radar[0]
            pygame.draw.line(screen, (0, 255, 0), self.center, position, 1)
            pygame.draw.circle(screen, (0, 255, 0), position, 5)

    def check_collision(self, game_map):
        self.alive = True
        for point in self.corners:
            #Meritum sprawdzenia wypadku, dotkniecie koloru sciany=wypadek
            #Przyjmujemy prostokat
            if game_map.get_at((int(point[0]), int(point[1]))) == BORDER_COLOR:
                self.alive = False
                break

    def check_radar(self, degree, game_map):
        length = 0
        x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
        y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)

        #Dopuki nie dotkniemy koloru sciany i dlugosc < 300 (przyjenty max) to poruszamy sie dalej
        while not game_map.get_at((x, y)) == BORDER_COLOR and length < 300:
            length = length + 1
            x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
            y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)

        #Kalkulujemy dystans do granicy i dodajemy do listy radarow
        dist = int(math.sqrt(math.pow(x - self.center[0], 2) + math.pow(y - self.center[1], 2)))
        self.radars.append([(x, y), dist])

    def update(self, game_map):
        #Ustawiamy predkosc na 15
        if not self.speed_set:
            self.speed = 15
            self.speed_set = True

        #Dostajemy obroconego ducha nastepnie ruszamy w kierunku x
        #Nie pozwalamy zbizyc sie do granicy bardziej niz 20px
        self.rotated_sprite = self.rotate_center(self.sprite, self.angle)
        self.position[0] += math.cos(math.radians(360 - self.angle)) * self.speed
        self.position[0] = max(self.position[0], 20)
        self.position[0] = min(self.position[0], WIDTH - 120)

        #Zwiekszamy czas i dystans
        self.distance += self.speed
        self.time += 1

        #Nie pozwalamy zbizyc sie do granicy bardziej niz 20px dla pozycji y
        self.position[1] += math.sin(math.radians(360 - self.angle)) * self.speed
        self.position[1] = max(self.position[1], 20)
        self.position[1] = min(self.position[1], WIDTH - 120)

        #Okreslamy nowy srodek
        self.center = [int(self.position[0]) + CAR_SIZE_X / 2, int(self.position[1]) + CAR_SIZE_Y / 2]

        #Obliczamy cztery narozniki
        #Dlugosc jest polowa boku
        length = 0.5 * CAR_SIZE_X
        left_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 30))) * length,
                    self.center[1] + math.sin(math.radians(360 - (self.angle + 30))) * length]
        right_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 150))) * length,
                     self.center[1] + math.sin(math.radians(360 - (self.angle + 150))) * length]
        left_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 210))) * length,
                       self.center[1] + math.sin(math.radians(360 - (self.angle + 210))) * length]
        right_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 330))) * length,
                        self.center[1] + math.sin(math.radians(360 - (self.angle + 330))) * length]
        self.corners = [left_top, right_top, left_bottom, right_bottom]

        #sprawdzamy kolizje i czyscimy radary
        self.check_collision(game_map)
        self.radars.clear()

        #Sprawdz radar co 45 dla od -90 do 120
        for d in range(-90, 120, 45):
            self.check_radar(d, game_map)

    def get_data(self):
        #Odczytujemy dystans do granicy
        radars = self.radars
        return_values = [0, 0, 0, 0, 0]
        for i, radar in enumerate(radars):
            return_values[i] = int(radar[1] / 30)

        return return_values

    def is_alive(self):
        #Podstawowa funkca istnienia
        return self.alive

    def get_reward(self):
        #Kalkulujemy nagrode 
        #Zwroc self.distance / 50.0
        return self.distance / (CAR_SIZE_X / 2)

    def rotate_center(self, image, angle):
        #Obracamy kwardrat
        rectangle = image.get_rect()
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_rectangle = rectangle.copy()
        rotated_rectangle.center = rotated_image.get_rect().center
        rotated_image = rotated_image.subsurface(rotated_rectangle).copy()
        return rotated_image


def run_simulation(genomes, config):
    #Puste kolekcje
    nets = []
    cars = []

    #inicjujemy PyGame i wyswietlamy
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    #Dla wszystkich genomow utworz nowa siec neuronowa
    for i, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0

        cars.append(Car())

    #Ustawienie zegara
    #Ustawienie czcionki & mapy
    clock = pygame.time.Clock()
    generation_font = pygame.font.SysFont("Arial", 30)
    alive_font = pygame.font.SysFont("Arial", 20)
    game_map = pygame.image.load('assets/map_easy.png').convert() 

    global current_generation
    current_generation += 1

    #Licznik do limitu czasu
    counter = 0

    while True:
        #Wyjscie
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        #wykonaj akcje dla kazdego samochodu
        for i, car in enumerate(cars):
            output = nets[i].activate(car.get_data())
            choice = output.index(max(output))
            if choice == 0:
                car.angle += 10  #Lewo o 10
            elif choice == 1:
                car.angle -= 10  #Prawo o 10
            elif choice == 2:
                if (car.speed - 2 >= 12):
                    car.speed -= 2  #zwolnij
            else:
                car.speed += 2  #przyspiesz

        #Sprawdzenie czy dalej zyje
        #Zwieksz still_alive jezeli zyje jezeli nie przerwij
        still_alive = 0
        for i, car in enumerate(cars):
            if car.is_alive():
                still_alive += 1
                car.update(game_map)
                genomes[i][1].fitness += car.get_reward()

        if still_alive == 0:
            break

        counter += 1
        if counter == 30 * 40:  #Skoncz po 20 sec
            break

        #Zaladuj mape i wszystkie zywe samochody
        screen.blit(game_map, (0, 0))
        for car in cars:
            if car.is_alive():
                car.draw(screen)

        #wyswietl info
        text = generation_font.render("Generation: " + str(current_generation), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (900, 450)
        screen.blit(text, text_rect)

        text = alive_font.render("Still Alive: " + str(still_alive), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (900, 490)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)  #dla 60 FPS


def play():
    pygame.display.set_caption("Symulation")
    #Zaladuj Config
    config_path = "./config.txt"
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                config_path)

    #Stworz populacje i dodaj reporterow
    population = neat.Population(config)
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    #Maksymalnie 1000 generacji
    population.run(run_simulation, 20)

    pygame.display.set_mode((1280, 720))
