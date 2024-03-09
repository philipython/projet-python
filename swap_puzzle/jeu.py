
from grid import Grid
from graph import Graph
import pygame
import random
from pygame.locals import *

import pygame

import random

class Grid:
    def __init__(self, rows, cols, difficulty):
        self.rows = rows
        self.cols = cols
        self.grid = self.create_random_grid(rows, cols, difficulty)

    def create_random_grid(self, rows, cols, difficulty):
        numbers = [i for i in range(1, rows*cols+1)]
        random.shuffle(numbers)

        grid = [[0 for _ in range(cols)] for _ in range(rows)]

        index = 0
        for row in range(rows):
            for col in range(cols):
                if index < len(numbers):
                    grid[row][col] = numbers[index]
                    index += 1

        for _ in range(difficulty):
            row1, col1 = random.randint(0, rows-1), random.randint(0, cols-1)
            row2, col2 = random.randint(0, rows-1), random.randint(0, cols-1)
            grid[row1][col1], grid[row2][col2] = grid[row2][col2], grid[row1][col1]

        return grid

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.grid])

class Game:
    def __init__(self):
        self.difficulty = None
        self.grid = None

    def choose_difficulty(self):
        print("Choisissez le niveau de difficulté :")
        print("1. Facile (3x3)")
        print("2. Moyen (4x4)")
        print("3. Difficile (5x5)")
        choice = input("Entrez le numéro correspondant au niveau de difficulté : ")

        if choice == '1':
            self.difficulty = 5
            self.grid = Grid(3, 3, self.difficulty)
        elif choice == '2':
            self.difficulty = 10
            self.grid = Grid(4, 4, self.difficulty)
        elif choice == '3':
            self.difficulty = 15
            self.grid = Grid(5, 5, self.difficulty)
        else:
            print("Choix invalide. Veuillez choisir un niveau de difficulté valide.")
            self.choose_difficulty()

    def play(self):
        self.choose_difficulty()
        print("Voici la grille de jeu :\n")
        print(self.grid)
        print("Déplacez les nombres pour les ordonner de manière croissante.\nUtilisez les touches 'w' pour monter, 'a' pour aller à gauche, 's' pour descendre et 'd' pour aller à droite.")

        while not self.is_solved():
            move = input("Entrez votre prochain mouvement (w/a/s/d) ou 'q' pour quitter : ")
            if move == 'q':
                print("Merci d'avoir joué !")
                return
            elif move in ['w', 'a', 's', 'd']:
                if self.make_move(move):
                    print("Mouvement valide !")
                else:
                    print("Mouvement invalide. Veuillez réessayer.")
            else:
                print("Mouvement invalide. Veuillez entrer 'w', 'a', 's', 'd' ou 'q'.")

    def is_solved(self):
        return self.grid.is_sorted()

    def make_move(self, direction):
        if direction == 'w':
            return self.grid.move_up()
        elif direction == 'a':
            return self.grid.move_left()
        elif direction == 's':
            return self.grid.move_down()
        elif direction == 'd':
            return self.grid.move_right()
        else:
            return False


# Initialisation et début du jeu
game = Game()
game.play()
