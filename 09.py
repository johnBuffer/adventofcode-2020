def solve1(d, s):
    for i in range(s, len(d)):
        if d[i] not in [(m + n) for j, m in enumerate(d[i-s:i]) for n in d[i-s+j+1:i]]:
            return d[i]

def solve2(d, t):
    a, b, s = 0, 0, 0
    while s != t:
        a, b, s = a + (s > t), b + (s < t), s - d[a] * (s > t) + d[b] * (s < t)
    return min(data[a:b]) + max(data[a:b])

data = [int(l) for l in open('09.data')]
print(solve1(data, 25))
print(solve2(data, solve1(data, 25)))
