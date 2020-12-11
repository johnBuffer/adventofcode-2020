def get_sight(row, col, grid, dr, dc, md):
    h, w, r, c, d, l = len(grid), len(grid[0]), row + dr, col + dc, 1, 2
    while h > r > -1 and w > c > -1 and d <= md and l > 1:
        r, c, d, l = r + dr, c + dc, d + 1, grid[r][c]
    return l%2

def get_count(row, col, grid, md):
    return sum([get_sight(row, col, grid, i, j, md) for i in [-1, 0, 1] for j in [-1, 0, 1] if i or j])

def next_state(current, occupied, max_seats):
    swap = (current == 0) * (occupied == 0) + (current == 1) * (occupied > max_seats)
    return 1 - current if swap else current 

def simulate(g, md, ms):
    return [[next_state(cl, get_count(r, c, g, md), ms) for c, cl in enumerate(rw)] for r, rw in enumerate(g)]

def solve(grid, last, md, ms):
    return sum(r.count(1) for r in grid) if grid == last else solve(simulate(grid, md, ms), grid, md, ms)

data = [[2 * (c == '.') for c in l.strip('\n')] for l in open('input')]
print(solve(data, None, 1, 3))
print(solve(data, None, max(len(data), len(data[0])), 4))
