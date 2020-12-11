from copy import deepcopy

def valid(row, col, grid):
    return len(grid) > row > -1 and len(grid[0]) > col > -1

def get_count(row, col, grid):
    offsets = [(row + i, col + j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
    return sum([grid[i][j] == '#' for i, j in offsets if valid(i, j, grid)])

def next_state(current, occupied):
    if current == 'L' and occupied == 0:
        return '#'
    if current == '#' and occupied > 3:
        return 'L'
    return current

def simulate(grid):
    next_grid = deepcopy(grid)
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            next_grid[i][j] = next_state(col, get_count(i, j, grid))
    return next_grid

def solve_1(grid):
    next_grid = simulate(grid)
    while grid != next_grid:
        grid = next_grid
        next_grid = simulate(grid)
    return sum([row.count('#') for row in grid])

data = [list(l.strip('\n')) for l in open('input')]
print(solve_1(deepcopy(data)))