
from grid import Grid
from graph import Graph
import pygame
import random
import sys


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def create_random_grid(size):
    numbers = random.sample(range(1, size*size+1), size*size)
    grid = [numbers[i:i + size] for i in range(0, size*size, size)]
    grid2 = Grid(size, size, grid)
    return grid2

class Game:
    def __init__(self, grid):
        self.grid = grid
        self.selected_row = -1
        self.selected_col = -1
        self.moves = 0
        # On doit passer ici une grille résolue pour calculer le chemin optimal.
        
        solved_state = [list(range(i * grid.n + 1, (i + 1) * grid.n )) for i in range(grid.m)]
        solved_grid = Grid(grid.m, grid.n, solved_state)

        # Calculer le nombre maximal de mouvements que l'utilisateur aura le droitt de faire via bfs_ter.
        path = grid.bfs_ter(solved_grid)
        if path is not None:
            self.max_moves = len(path)
        else:
            print("problem with bfs")
            self.max_moves = sys.maxsize

    def draw(self, screen):
        tile_width = WINDOW_WIDTH // self.grid.n
        tile_height = WINDOW_HEIGHT // self.grid.m

        for row in range(self.grid.m):
            for col in range(self.grid.n):
                tile_value = self.grid.state[row][col]
                rect = pygame.Rect(col * tile_width, row * tile_height, tile_width, tile_height)
                pygame.draw.rect(screen, BLACK, rect, 3)

                inner_rect = rect.inflate(-6, -6)
                pygame.draw.rect(screen, WHITE, inner_rect)

                font = pygame.font.Font(None, 36)
                text = font.render(str(tile_value), True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

                if self.selected_row == row and self.selected_col == col:
                    pygame.draw.rect(screen, RED, rect, 5)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            self.selected_row = mouse_pos[1] // (WINDOW_HEIGHT // self.grid.m)
            self.selected_col = mouse_pos[0] // (WINDOW_WIDTH // self.grid.n)
        
        elif event.type == pygame.KEYDOWN and self.selected_row >= 0 and self.selected_col >= 0:
            if self.move_tile(event.key):
                self.moves += 1

    def move_tile(self, key):
        delta = {pygame.K_UP: (-1, 0), pygame.K_DOWN: (1, 0), pygame.K_LEFT: (0, -1), pygame.K_RIGHT: (0, 1)}
        if key in delta:
            dx, dy = delta[key]
            new_row = self.selected_row + dx
            new_col = self.selected_col + dy
            if 0 <= new_row < self.grid.m and 0 <= new_col < self.grid.n:
                self.grid.swap((self.selected_row, self.selected_col), (new_row, new_col))
                self.selected_row, self.selected_col = new_row, new_col
                return True
        return False

    def check_game_over(self, screen):
        # Si la grille est triée et que le nombre de mouvements est égal au nombre minimal de swaps,
        # l'utilisateur gagne. Sinon, s'il dépasse ce nombre, il perd.
        if self.grid.is_sorted():
            if self.moves == self.max_moves:
                font = pygame.font.Font(None, 74)
                text = font.render('You win!', True, RED)
                text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
                screen.blit(text, text_rect)
                pygame.display.flip()
                pygame.time.wait(3000)
                return "win"
            else:
                # Afficher un message indiquant que l'utilisateur a résolu la grille, 
                # mais pas avec le nombre minimal de swaps.
                font = pygame.font.Font(None, 74)
                text = font.render('Optimal solution not achieved!', True, RED)
                text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
                screen.blit(text, text_rect)
                pygame.display.flip()
                pygame.time.wait(3000)
                return "continue" 
        elif self.moves > self.max_moves:
            font = pygame.font.Font(None, 74)
            text = font.render('You lose!', True, RED)
            text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(3000)
            return "lose"
        return "continue"

def choose_difficulty():
    difficulty = input("Choose difficulty - Easy (3x3), Medium (4x4), Hard (5x5): ").strip().lower()
    size = 3  
    if difficulty == 'medium':
        size = 4
    elif difficulty == 'hard':
        size = 5
    return size

# Initialisation de Pygame
pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Puzzle Game")

# Demander à l'utilisateur de choisir la difficulté avant de lancer le jeu
grid_size = choose_difficulty()
initial_grid = create_random_grid(grid_size)
game = Game(initial_grid)

# Boucle principale du jeu
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            game.handle_event(event)

    game_status = game.check_game_over(screen)
    if game_status in ["win", "lose"]:
        running = False

    game.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()

