"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
import pygame
from collections import deque
import math 
import matplotlib.pyplot as plt 
from graph import Graph
from heapq import heappop, heappush
import copy


class GridVisualizer: # Defines a class to visualize a grid using Pygame
    def __init__(self, grid):
        """
        Initializes the grid visualizer.
        
        grid: 2D list representing the grid state
        cell_size: Size of each cell in pixels
        grid_color: Color of the grid lines (R, G, B)
        """
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.cell_size = 50 # Sets a  cell size of 50 pixels for the grid
        self.grid_color = (0,0,0) # grid line color : black
        

        self.width = self.n * self.cell_size #Calculates the Pygame window width based on the number of columns and cell size
        self.height = self.m * self.cell_size #Calculates the Pygame window height based on the number of rows and cell size
        
        
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height)) #Creates the display window with the calculated dimensions
        pygame.display.set_caption("Grid Representation") # sets a title
        
        
        self.background_color = (255, 255, 255) # background color of the screen : white
    
    def draw_grid(self):
        """
        Draws the grid on the window, filling each cell with its value.
        """
        #Fills the screen background with the background color (white)
        self.screen.fill(self.background_color) 

        # Initialize the style of writting.
        font = pygame.font.Font(None, 24)
        
        for i in range(self.m):
            for j in range(self.n):
                # Retrieve the value of the current cell
                cell_value = self.grid[i][j]
                
                # Define the rectangle for the current cell.
                rect = pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                # Draw the cell rectangle using the grid color.
                pygame.draw.rect(self.screen, self.grid_color, rect, 1)
                
                # Render the cell value as text
                text = font.render(str(cell_value), True, (0, 0, 0))
                # Get the position to center the text in the rectangle
                text_pos = text.get_rect(center=rect.center)
                
                # put the text at the caalculated position
                self.screen.blit(text, text_pos)

        # Update the display to show the new grid
        pygame.display.flip()


    def run(self):
        """
        Main loop for the grid visualizer.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Draw the updated grid each loop iteration
            self.draw_grid()
            
        pygame.quit()
        
     



class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state


    def __str__(self):
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    '''
    # representation with pygame
    def __str__(self):
        """Use the class GridVisualizer to visualize the grid"""

        visualizer = GridVisualizer(self.state)
        visualizer.run()
        return ""
    '''
    
    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"
    

    """ 
    Question 2
    """
    
    def is_sorted(self):
        """
        Checks if the current state of the grid is sorted and returns the answer as a boolean.
        """
        # Check if the numbers in each line are sorted
        for i in range(self.m):
            for j in range(self.n - 1):
                if self.state[i][j] > self.state[i][j+1]:
                    return False
                
        # Check if the jumps from one line to the next preserve the order
        for i in range(0, self.m - 1):
            if self.state[i][-1] > self.state[i+1][0]:
                return False
        return True

    
    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        i1, j1 = cell1
        i2, j2 = cell2
        if (abs(i1-i2)==0 and abs(j1-j2)==1) or (abs(i1-i2)==1 and abs(j1-j2)==0):
             self.state[i1][j1], self.state[i2][j2] = self.state[i2][j2], self.state[i1][j1]
        else:
            raise Exception("the two cells are not next to each other")
        return self
    
    
    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for cell_1, cell_2 in cell_pair_list:
            self.swap(cell_1, cell_2)
        return self

        
    """ 
    Question 4 : Représentation graphique
    """
    
    def trace(self):
        _, ax = plt.subplots()
        ax.matshow(self.state, cmap=plt.cm.Blues)
        for i in range(self.n):
            for j in range(self.m):
                c = self.state[j][i]
                ax.text(i, j, str(c), va='center', ha='center')
        plt.show()

        

    
    """ 
    Question 6 : transformation des noeuds en type d objets hachables 
    """
    
    def make_hashable(self):
        """
        Tuples are hashable, so just convert the graph to a tuple
        """
        list_tuples = (tuple(self.state[i]) for i in range(self.m))
        tuple_tuples = tuple(list_tuples)
        return tuple_tuples


    """ 
    Question 7 : creation de bfs pour le swapp_puzzle
    """

    """ 
    We create an initial function that implements all possible states of the grid to create all possible nodes. 
    """ 
    def grids_graph(self):
        m = self.m
        n = self.n
        from itertools import permutations
        """
        function to create all possible arrangements of numbers from 1 to m*n 
        """
        all_permutations = permutations(range(1, n*m + 1))
        tuples = []
        for permutation in all_permutations:
            perm_lines = [permutation[n*i:n*(i+1)] for i in range(m)]
            perm_tuple = tuple(tuple(line) for line in perm_lines)
            tuples.append(perm_tuple)
        return tuples


    """
    We create a function that implements all the edges possible between all the nodes (only one swap between a grid and another)
    """
    def all_edges(self):
        if not hasattr(self, "path_graph"): # Checks if path_graph attribute exists in the object; if not, it initializes it
            self.path_graph = Graph(self.grids_graph()) #Creates a Graph with all possible grid states.
        nodes = self.path_graph.nodes
        from copy import deepcopy # to copy the grid to make transpositions possible
        m = len(nodes[0])
        n = len(nodes[0][0])
        list_transpositions = [((i,j),(i,j+1)) for i in range(m) for j in range(n-1)] + [((i,j),(i+1,j)) for i in range(m-1) for j in range(n)] #Creates a list of all possible cell swaps (transpositions) within the grid
        list_edges = set()
        for node in nodes:
            # Find all possible neighbors
            node_list = [list(line) for line in node] # transforme to make mutable
            for transposition in list_transpositions:
                target = deepcopy(node_list) 
                ((i_0, j_0), (i_1, j_1)) = transposition # Unpacks the row and column indices for swapping cells
                target[i_0][j_0], target[i_1][j_1] = target[i_1][j_1], target[i_0][j_0] # makes the swap
                target_tuple = tuple(tuple(line) for line in target)
                list_edges.add((node, target_tuple)) #Adds the edge to the set
                list_edges.add((target_tuple, node)) # adds the edge in the other way 
        return list(list_edges)

    """
    We can create a complete graph from the grid
    We will apply BFS to the grid, starting from 'self' (the current grid), and aiming for the solved grid
    We will find the best path between the current grid and the solved one
    """
    
    def find_best_path(self):
        if not hasattr(self, "path_graph"):
            path_graph_nodes = self.grids_graph()
            self.path_graph = Graph(path_graph_nodes)
            self.path_graph.edges = self.all_edges()
            # We do not completely fulfill the graph attributes because it is not useful
        n = self.n
        m = self.m
        solved = tuple(tuple(range(n*i+1,n*(i+1)+1)) for i in range(m))
        current = tuple(tuple(line) for line in self.state)
        return self.path_graph.bfs(current, solved)
    

    #create an object from a file (a grid is created with a file)
    @classmethod # method which has an impact on the class itself
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid



    def bfs_bis(self, dst):
        # Initialize a graph with the current grid state as a node
        dico = Graph([self.make_hashable()])
        m, n = self.m, self.n
        # Initialize a queue with tuples containing the current state and its path
        file = deque([(self.make_hashable(), [self.make_hashable()])])
        # Convert the destination grid to a hashable type
        ndst = dst.make_hashable()

        while file:
            # Remove and return the leftmost path
            s, path = file.popleft()
            # Check if the current path's endpoint is the destination
            if s == ndst:
                return path
            save = copy.deepcopy(self.state)
            # Explore all possible moves from the current state
            for i in range(m):
                for j in range(n):
                    self.state = copy.deepcopy(save)
                    # Check all four directions where a swap can happen
                    # Swapping with the cell below
                    if i < m - 1:
                        # Create a new grid state by swapping and convert it to hashable
                        bas = self.swap_seq([((i, j), (i + 1, j))])
                        h_bas = bas.make_hashable()
                        # Add a new edge if this state is new
                        if h_bas not in dico.graph[s]:
                            dico.add_edge(s, h_bas)

                    # Swapping with the cell to the right
                    if j < n - 1:
                        droite = self.swap_seq([((i, j), (i, j + 1))])
                        h_droite = droite.make_hashable()
                        if h_droite not in dico.graph[s]:
                            dico.add_edge(s, h_droite)


            # Add new states to explore to the queue
            for i in dico.graph[s]:
                if i not in path:
                    file.append((i, path + [i]))
                
        return None

   
    def heuristique0(self):
        misplaced_count = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.state[i][j] != j + self.n * i + 1:  
                    misplaced_count += 1
        # Return the total distance divided by 2 to ensure it is less than real distance
        return misplaced_count/2

    @staticmethod
    def trouver_coordonnees(liste, element):
        # Find the coordinates of an element in the grid
        for i, sous_liste in enumerate(liste):
            if element in sous_liste:
                # Return the coordinates once the element is found.
                return i, sous_liste.index(element)
        # Return None if the element is not found
        return None



    def heuristique1(self):
        # Calculate heuristic based on the Manhattan distance for each tile to its target location.
        n, m, l = self.n, self.m, self.state
        k=0
        dist = 0
        # Iterate to compute Manhattan distance for each tile.
        for i in range(m):
            for j in range(n):
                k += 1
                # Find the current position of k and calculate Manhattan distance.
                x, y = self.trouver_coordonnees(l, k)
                dist += abs(x - i) + abs(y - j)
        # Return the total distance divided by 2 to ensure it is less than real distance
        return dist/2



    def bfs_ter(self, dst):
        # Initialisation avec l'état actuel de la grille et un chemin vide.
        file = [(self.heuristique1(), [], self)]
        visited = set([self.make_hashable()])  
        hash_dst = dst.make_hashable()
        while file:
            _, path, current_grid = heappop(file)
            current_state = current_grid.make_hashable()

            if current_state == hash_dst:
                return path  # Retourne le chemin sous forme de swaps

            for i in range(self.m):
                for j in range(self.n):
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        x, y = i + dx, j + dy
                        if 0 <= x < self.m and 0 <= y < self.n:
                            new_grid = copy.deepcopy(current_grid)
                            if (abs(i - x) == 1 and j == y) or (abs(j - y) == 1 and i == x):
                                new_grid.swap((i, j), (x, y))
                                new_state = new_grid.make_hashable()

                                if new_state not in visited:
                                    visited.add(new_state)
                                    new_path = path + [((i, j), (x, y))]
                                    heappush(file, (new_grid.heuristique1() + len(new_path), new_path, new_grid))

        return None  # Retourne None si aucun chemin n'est trouvé