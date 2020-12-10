def solve_1(data):
    offsets = [data[i+1] - m for i, m in enumerate(data[:-1])] + [3]
    return offsets.count(1) * offsets.count(3)

def solve_2(idx, d, t):
    if t - d[idx] < 4:
        return 1
    return sum([solve_2(idx+i, d, t) for i in range(1, 4) if (idx + i < len(d)) and (d[idx + i] - d[idx] < 4)])

data = [0] + sorted([int(l) for l in open('input')])
print(solve_1(data))
print(solve_2(0, data, max(data) + 3))
