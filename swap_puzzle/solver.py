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
        big_list_moves = []


        # 1. Find the element
        def find_element(element, grid):
            for i in range(grid.m):
                for j in range(grid.n):
                    if grid.state[i][j] == element:
                        return (i, j)

        # 2. For each line, give it the elements it should contain
        def align_element_in_line(grid, line_index, current_column, shift, list_moves = []):
            """We shift the column of an element in some line recursively
            Input:
            - line: the list of elements in the line. Is obtained with grid.state[i]
            - current_position: index of the element to be shifted in the list
            - shift: the shift to be applied
            - list_moves: should be left blank. Used as an argument for the recursion
            Output:
            - The list of moves performed.
            """
            line = grid.state[line_index]
            if shift == 0:
                return list_moves
            else:
                if shift >= 1:
                    
                    line[current_column], line[current_column + 1] = line[current_column + 1], line[current_column]
                    list_moves.append(((line_index, current_column),(line_index, current_column + 1)))
                    return align_element_in_line(grid, line_index, current_column + 1, shift - 1, list_moves)
                if shift <= -1:
                    line[current_column-1], line[current_column] = line[current_column], line[current_column-1]
                    list_moves.append(((line_index, current_column),(line_index, current_column - 1)))
                    return align_element_in_line(grid, line, current_column - 1, shift + 1, list_moves)

        def get_elements_for_line(grid, line_index,):
            """Brings the elements [line*self.grid.n, ... (line+1)*self.grid.n - 1] on the line line_index."""
            big_list_moves = []
            # The line has elements [line*self.grid.n, ... (line+1)*self.grid.n - 1]
            list_elements = list(range(line_index*grid.n+1, (line_index+1)*grid.n+1)) # The numbers start at 1
            print(f"{list_elements=}")
            #  All elements that are supposed to be on this line/
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
                    big_list_moves += align_element_in_line(grid, l_good, c_good, c_bad-c_good)
                    if l_good > line_index:
                        sign = -1
                    else:
                        sign = 1
                    list_moves = [((l,c_bad),(l+sign, c_bad)) for l in range(l_good, line_index, sign)]
                    grid.swap_seq(list_moves)
                    big_list_moves += list_moves
            return big_list_moves

        # Now put all elements in the right lines:
        for line_index in range(self.grid.m):
            big_list_moves += get_elements_for_line(self.grid, line_index)
        
        def sort_all_lines(grid):
            list_moves = []
            for i in range(self.grid.m):
                for j in range(self.grid.n-1):
                    if grid.state[i][j] > grid.state[i][j+1]:
                        list_moves.append(((i,j),(i,j+1)))
                        grid.state[i][j], grid.state[i][j+1] = grid.state[i][j+1], grid.state[i][j]
            return list_moves

        while not self.grid.is_sorted():
            big_list_moves += sort_all_lines(self.grid)

        return big_list_moves