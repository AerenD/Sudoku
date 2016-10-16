class Sudoku:

    def __init__(self, sudoku):
        self.board = sudoku  # List of nine lists (rows) in a sudoku board
        self.solution = []   # Solution, will only contain one solution
        self.solve()         # Start recursive call to solve board

    # Print the board to the console
    def print_board(self, board):
        for row in board:
            for number in row:
                print("{}".format(number), end=" ")
            print()
        print()

    # Finds the next cell that contains a zero (not a real sudoku term)
    def find_next_cell(self, x, y):
        for x in range(x, 9):  # Start on the current row at the current position
            if self.get(x, y) == 0:
                return x, y
        for y in range(y, 9):  # Iterate over other rows
            for x in range(0, 9):
                if self.get(x, y) == 0:
                    return x, y
        return False

    # Test if the proposed sudoku term is valid
    def is_valid(self, value, x, y):
        if value not in self.get_row(y):
            if value not in self.get_col(x):
                if value not in self.get_block(x, y):
                    return True
        return False

    # Recursive loop that uses brute force over unknown cells to solve
    def solve(self, x=0, y=0):
        if self.find_next_cell(x, y):         # Find the next cell to solve
            x, y = self.find_next_cell(x, y)  # Returns location of next cell
            for i in range(1, 10):            # Iterates over possible entries
                if self.is_valid(i, x, y):    # Check whether entry is valid
                    self.put(i, x, y)         # Add valid entry to board
                    self.solve(x, y)          # Recursive call to repeat
            self.put(0, x, y)                 # If failed, remove tested entry
        else:
            board = []                        # Need to create new board to append to avoid
            for line in self.board:           # problems with appending and list references
                board.append(line[:])         # Append slice to avoid using a list reference
                self.solution = board         # Add new board to solutions (currently only one possible)

    # Returns value of specified location
    def get(self, x, y):
        return self.board[y][x]

    # Adds value to specified location
    def put(self, value, x, y):
        self.board[y][x] = value

    # Returns list of all values in the same row
    def get_row(self, row_num):
        row = self.board[row_num]
        return row

    # Returns list of all values in the same column
    def get_col(self, col_num):
        col = [row[col_num] for row in self.board]
        return col

    # Returns list of all values in the same block
    def get_block(self, x, y):
        if x in range(0, 3):                     # Determine whether x-value falls in first range
            col_num = range(0, 3)
        elif x in range(3, 6):                   # Determine whether x-value falls in second range
            col_num = range(3, 6)
        else:                                    # Determine whether x-value falls in third range
            col_num = range(6, 9)

        if y in range(0, 3):                     # Determine whether y-value falls in first range
            block = []
            for row in self.board[0: 3]:         # Iterate over rows in y-range
                row = [row[i] for i in col_num]  # Add values from x-range to block
                block = block + row
            return block

        elif y in range(3, 6):                   # Determine whether x-value falls in second range
            block = []
            for row in self.board[3: 6]:         # Iterate over rows in y-range
                row = [row[i] for i in col_num]  # Add values from x-range to block
                block = block + row
            return block

        else:                                    # Determine whether x-value falls in third range
            block = []
            for row in self.board[6: 9]:         # Iterate over rows in y-range
                row = [row[i] for i in col_num]  # Add values from x-range to block
                block = block + row
            return block

""" Sample Boards

sudoku_board = [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]

# Board Easy
sudoku_board = [[0,3,0,9,5,2,0,7,0],
                [0,9,1,0,0,0,2,5,8],
                [7,0,2,0,1,8,0,3,0],
                [9,0,3,0,0,6,7,0,5],
                [0,2,0,7,4,0,0,6,9],
                [1,0,6,5,3,0,0,0,2],
                [5,1,0,4,0,0,8,2,0],
                [0,0,0,1,6,7,0,9,3],
                [3,6,9,8,0,0,1,0,0]]

# Board Expert
sudoku_board = [[0,7,0,0,0,6,0,0,0],
                [0,0,0,4,7,0,0,5,0],
                [2,0,9,8,0,0,0,0,0],
                [0,0,3,0,0,0,0,2,0],
                [7,4,0,0,0,0,0,0,8],
                [0,0,0,0,0,2,6,0,1],
                [0,0,0,0,0,0,0,0,0],
                [0,8,5,0,0,0,0,1,9],
                [0,3,6,5,0,8,0,0,0]]
"""

sudoku_board = [[0,7,0,0,0,6,0,0,0],
                [0,0,0,4,7,0,0,5,0],
                [2,0,9,8,0,0,0,0,0],
                [0,0,3,0,0,0,0,2,0],
                [7,4,0,0,0,0,0,0,8],
                [0,0,0,0,0,2,6,0,1],
                [0,0,0,0,0,0,0,0,0],
                [0,8,5,0,0,0,0,1,9],
                [0,3,6,5,0,8,0,0,0]]

if __name__ == '__main__':
    s = Sudoku(sudoku_board)
    print(s.print_board(s.solution))

