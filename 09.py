def solve1(data, s):
    for i in range(s, len(data)):
        if data[i] not in [(m + n) for j, m in enumerate(data[i-s:i]) for n in data[i-s+j+1:i]]:
            return data[i]

def solve2(d, t):
    a, b, s = 0, 1, d[0]
    while s != t:
        a, b, s = a + (s > t), b + (s < t), s - d[a] * (s > t) + d[b] * (s < t)
    return min(data[a:b]) + max(data[a:b])

data = [int(l) for l in open('09.data')]
print(solve1(data, 25))
print(solve2(data, solve1(data, 25)))
