from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """
    def __init__(self, grid):
        self.grid = grid

    def get_solution(self):

    
    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        solution = []
        for i in range(self.grid.m):
            for j in range(self.grid.n - 1):
                if self.grid.state[i][j] > self.grid.state[i][j + 1]:
                    self.grid.swap((i, j), (i, j + 1))
                    solution.append(((i, j), (i, j + 1)))
        return solution
        
       """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        raise NotImplementedError
        """


