def loadData(day):
	return [l for l in open('{}.data'.format(day), 'r')]


def solve1():
    grid = loadData('03')

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    # cimer windows
    width =  (len(grid[0]) - 1)

    res = 1
    for dx, dy in slopes:
        x = 0
        y = 0
        trees = 0
        while y < len(grid):
            l = grid[y]
            if l[x % width] == '#':
                trees += 1

            x += dx
            y += dy

        res *= trees
        
    return res

print(solve1())