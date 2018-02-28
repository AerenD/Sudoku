def solve(board):
    "Returns the solved sudoku board, not all boards are solvable"
    next_empty = _next_empty(board)
    if not next_empty:
        return board

    row, col = next_empty
    peers = (set(_row(board, row, col))
             | set(_col(board, row, col))
             | set(_block(board, row, col)))
    for guess in range(1, 10):
        if guess not in peers:
            board[row][col] = guess
            solution = solve(board)
            if solution:
                return solution
    board[row][col] = 0


def _next_empty(board):
    "Returns the coordinates of the next empty cell in the sudoku board."
    for row in range(9):
        for col in range(9):
            if not board[row][col]:
                return (row, col)
    return None


def _row(board, row, col):
    "Returns a list of all items in the same row as the given position."
    return board[row]


def _col(board, row, col):
    "Returns a list of all items in the same column as the given position."
    return [row[col] for row in board]


def _block(board, row, col):
    "Returns a list of all items in the same block as the given position."
    rows = range((row // 3) * 3, (row // 3) * 3 + 3)
    cols = range((col // 3) * 3, (col // 3) * 3 + 3)
    return [board[row][col] for row in rows for col in cols]


if __name__ == '__main__':
    board = [[0, 7, 0, 0, 0, 6, 0, 0, 0],
             [0, 0, 0, 4, 7, 0, 0, 5, 0],
             [2, 0, 9, 8, 0, 0, 0, 0, 0],
             [0, 0, 3, 0, 0, 0, 0, 2, 0],
             [7, 4, 0, 0, 0, 0, 0, 0, 8],
             [0, 0, 0, 0, 0, 2, 6, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 5, 0, 0, 0, 0, 1, 9],
             [0, 3, 6, 5, 0, 8, 0, 0, 0]]

    solution = solve(board)
    for row in solution:
        for cell in row:
            print(cell, end=' ')
        print()
