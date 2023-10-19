def is_valid_in_row(grid, row, num):
    for col in range(9):

        if grid[row][col] == num:
            return False

    return True


def is_valid_in_col(grid, col, num):
    for row in range(9):

        if grid[row][col] == num:
            return False

    return True


def is_valid_in_subgrid(grid, row, col, num):
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True


def is_valid(grid, row, col, num):
    return is_valid_in_row(grid, row, num) and is_valid_in_col(grid, col, num) and is_valid_in_subgrid(grid, row, col,
                                                                                                       num)


def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None


def count_solutions(grid):
    cell = find_empty_cell(grid)
    if cell == None:
        return 1
    row, col = cell
    count = 0
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            count += count_solutions(grid)
            grid[row][col] = 0
    return count


def read_grid():
    grid = []
    for i in range(9):
        row = list(map(int, input().split()))
        grid.append(row)
    return grid


grid = read_grid()
print(count_solutions(grid))
