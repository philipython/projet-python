from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """
    def __init__(self, grid):
        self.grid = grid

    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # 1. Find the element
        def find_element(element, grid):
            for i in range(grid.m):
                for j in range(grid.n):
                    if grid.state[i][j] == element:
                        return (i, j)
                        
        # 2. For each line, give it the elements it should contain
        def align_element_in_line(line, current_column, shift, list_moves = []):
            if shift == 0:
                return list_moves
            else:
                if shift >= 1:
                    line[current_column], line[current_column + 1] = line[current_column + 1], line[current_column]
                    list_moves.append(((line, current_column),(line, current_column + 1)))
                    return align_element_in_line(line, current_column + 1, shift - 1, list_moves)
                if shift <= -1:
                    line[current_column-1], line[current_column] = line[current_column], line[current_column-1]
                    list_moves.append(((line, current_column),(line, current_column - 1)))
                    return align_element_in_line(line, current_column - 1, shift + 1, list_moves)"
                    
                    
        def get_elements_for_line(grid, line_index,):
            """Brings the elements [line*self.grid.n, ... (line+1)*self.grid.n - 1] on the line line_index."""
            big_list_moves = []
            # The line has elements [line*self.grid.n, ... (line+1)*self.grid.n - 1]
            list_elements = list(range(line_index*grid.n+1, (line_index+1)*grid.n+1)) # The numbers start at 1
            print(f\"{list_elements=}\")
            #  All elements that are supposed to be on this line
            for element in list_elements:
                # Find where it is.
                l_good, c_good = find_element(element, grid)
                if l_good != line_index:
                    # Look for a column in line line_index that contains a bad element
                    for column, element in enumerate(grid.state[line_index]):
                        if not element in list_elements:
                            c_bad = column
                            break # Get out of the for loop when we find one.
                    # Now we have the column of a bad element in line_index. Move the element at position i, j to position i, column_bad_element.
                    big_list_moves += align_element_in_line(grid.state[l_good], c_good, c_bad-c_good)
                    if l_good > line_index:
                        sign = -1
                    else:
                        sign = 1
                    list_moves = [((l,c_bad),(l+sign, c_bad)) for l in range(l_good, line_index, sign)]
                    grid.swap_seq(list_moves)
                    big_list_moves += list_moves
            return big_list_moves

        for line_index in range(grid.m):
            get_elements_for_line(grid, line_index)
            # Maintenant que chaque ligne contient les bons éléments, trier
        max_index = 0
        while not grid.is_sorted():
            max_index += 1
            if max_index > 100:
                break
            for line_index in range(grid.m):
                solution = []
                for i in range(self.grid.m):
                    for j in range(self.grid.n - 1):
                        if self.grid.state[i][j] > self.grid.state[i][j + 1]:
                            self.grid.swap((i, j), (i, j + 1))
                            solution.append(((i, j), (i, j + 1)))
                return solution
        # A la fin, tout est trié parce que is_sorted le montre.


