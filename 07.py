def loadData(day):
	return [l for l in open('{}.data'.format(day), 'r')]

def parseRule(line):
    # Remove the dot
    parts = line.strip('\n')[:-1].split('bags contain')
    name = parts[0].strip()
    subs = []
    if parts[1].find("no other bags") == -1:
        for s in parts[1].split(','):
            count, bag = s.strip().split(' ', 1)
            subs.append((int(count), bag[:bag.rfind(' ')]))
    return name, subs

def canContain(outer, inner, rules):
    rule = rules.get(outer, [])
    return sum(b == inner or canContain(b, inner, rules) for _, b in rule)

def count(bag, rules):
    rule = rules.get(bag, None)
    return sum(c * (count(b, rules) + 1) for c, b in rule)

def solve1():
    rules = dict(parseRule(l) for l in loadData('07'))
    return sum(canContain(r, "shiny gold", rules) > 0 for r in rules.keys())

def solve2():
    rules = dict(parseRule(l) for l in loadData('07'))
    return count("shiny gold", rules)

print(solve1())
print(solve2())
