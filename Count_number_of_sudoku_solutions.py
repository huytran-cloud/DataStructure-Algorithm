def is_valid(board, row, col, num):
    # Check if the number already exists in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number already exists in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number already exists in the 3x3 sub-grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Undo the current placement
                return False  # No valid number found
    return True  # All cells filled, solution found


def count_sudoku_solutions(board):
    count = [0]  # Counter to keep track of the number of solutions

    def solve(board, count):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve_sudoku(board):
                                count[0] += 1
                            board[row][col] = 0  # Undo the current placement
                    return

    solve(board, count)
    return count[0]


# Test the function
board = []
for _ in range(9):
    row = list(map(int, input().split()))
    board.append(row)

solution_count = count_sudoku_solutions(board)
print(solution_count)