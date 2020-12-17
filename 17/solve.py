def offs(c, i=0):
    return [tuple(c)] if len(c)==i else offs(c, i+1) + offs(c[:i] + [c[i]+1] + c[i+1:], i+1) + offs(c[:i] + [c[i]-1] + c[i+1:], i+1)

# def offs_2(c, i=0, l=-1, u=1):
#     if len(c)==i:
#         return tuple(c)
#     else:
#         for x in range(l, u+1):
#             offs(c, i+1)

def ns(p, c, data):
    a = sum(data.get(ps, 0) for ps in offs(list(p))) - c
    return 1 - c if (c and (a < 2 or a > 3)) or (c == 0 and a == 3) else c

def iterate_1(g, dim, i):
    w, h, d = dim
    return {(x, y, z): ns((x, y, z), g.get((x, y, z), 0), g) for x in range(-i, w+i) for y in range(-i, h+i) for z in range(-i, d+i)}

def iterate_2(g, dim, i):
    w, h, d, t = dim
    return {(x, y, z, f): ns((x, y, z, f), g.get((x, y, z, f), 0), g) for x in range(-i, w+i) for y in range(-i, h+i) for z in range(-i, d+i) for f in range(-i, t+i)}

def solve(data, dim, count, fun):
    for i in range(count): data = fun(data, dim, i+1)
    return sum(v for v in data.values())

lines = [l.strip('\n') for l in open('input')]
dim = (len(lines[0]), len(lines), 1)
# Part 1
print(solve({(x, y, 0): v=='#' for y, l in enumerate(lines) for x, v in enumerate(l)}, dim, 6, iterate_1))
# Part 2
print(solve({(x, y, 0, 0): v=='#' for y, l in enumerate(lines) for x, v in enumerate(l)}, dim + tuple([1]), 6, iterate_2))

