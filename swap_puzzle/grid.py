"""
This is the grid module. It contains the Grid class and its associated methods.
"""


import random
import pygame
class GridVisualizer:
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
        self.cell_size = 50
        self.grid_color = (0,0,0)
        

        self.width = self.n * self.cell_size
        self.height = self.m * self.cell_size
        

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Grid Representation")
        

        self.background_color = (255, 255, 255)
    
    def draw_grid(self):
        """
        Draws the grid on the window, filling each cell with its value.
        """
        self.screen.fill(self.background_color)
        

        font = pygame.font.Font(None, 24)
        
        for i in range(self.m):
            for j in range(self.n):
                cell_value = self.grid[i][j]
                

                rect = pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, self.grid_color, rect, 1)
                

                text = font.render(str(cell_value), True, (0, 0, 0))

                text_pos = text.get_rect(center=rect.center)
                

                self.screen.blit(text, text_pos)
                
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
        Prints the state of the grid as text :
        
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output
        """
        """
        Prints the state of the grid as a grid
        """
        self.visualizer = GridVisualizer(self.state)
        self.visualizer.run()

    
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
        Checks is the current state of the grid is sorted and returns the answer as a boolean.
        """
        for i in range(self.m):
            for j in range(self.n - 1):
                if self.state[i][j] > self.state[i][j+1]:
                    return False
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
        list_tuples = [tuple(self.state[i]) for i in range(self.m)]
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
        

    def all_edges(self):
        if not hasattr(self, "path_graph"):
            self.path_graph = Graph(self.grids_graph())
        nodes = self.path_graph.nodes
        from copy import deepcopy
        m = len(nodes[0])
        n = len(nodes[0][0])
        list_transpositions = [((i,j),(i,j+1)) for i in range(m) for j in range(n-1)] + [((i,j),(i+1,j)) for i in range(m-1) for j in range(n)]
        list_edges = set()
        for node in nodes:
            # Find all possible neighbors
            node_list = [list(line) for line in node]
            for transposition in list_transpositions:
                target = deepcopy(node_list)
                ((i_0, j_0), (i_1, j_1)) = transposition
                target[i_0][j_0], target[i_1][j_1] = target[i_1][j_1], target[i_0][j_0]
                target_tuple = tuple(tuple(line) for line in target)
                list_edges.add((node, target_tuple))
                list_edges.add((target_tuple, node))
        return list(list_edges)
        
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
