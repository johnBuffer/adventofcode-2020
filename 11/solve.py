from copy import deepcopy

def valid(row, col, grid):
    return len(grid) > row > -1 and len(grid[0]) > col > -1

def get_sight(row, col, grid, direction, mxd):
    r, c, d = row + direction[0], col + direction[1], 1
    while valid(r, c, grid) and d <= mxd:
        if grid[r][c] == "#":
            return 1
        if grid[r][c] == "L":
            return 0
        r, c, d = r + direction[0], c + direction[1], d + 1
    return 0

def get_count(row, col, grid, max_dist):
    offsets = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
    return sum([get_sight(row, col, grid, (i, j), max_dist) for i, j in offsets])

def next_state(current, occupied, max_seats):
    if current == 'L' and occupied == 0:
        return '#'
    if current == '#' and occupied > max_seats:
        return 'L'
    return current

def simulate_1(grid_1, grid_2, max_dist, max_seats):
    for r, row in enumerate(grid_1):
        for c, col in enumerate(row):
            grid_2[r][c] = next_state(col, get_count(r, c, grid_1, max_dist), max_seats)
    return grid_1, grid_2

def solve(grid, max_dist, max_seats):
    next_grid = deepcopy(grid)
    grid, next_grid = simulate_1(grid, next_grid, max_dist, max_seats)
    for r in next_grid:
        print(''.join(r))
    print()
    while grid != next_grid:
        grid, next_grid = simulate_1(next_grid, grid, max_dist, max_seats)
        for r in next_grid:
            print(''.join(r))
        print()
    return sum([row.count('#') for row in grid])


data = [list(l.strip('\n')) for l in open('input')]
#print(solve(deepcopy(data), 1, 3))
print(solve(deepcopy(data), max(len(data), len(data[0])), 4))
