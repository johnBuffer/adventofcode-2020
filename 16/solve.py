import math

def load_data():
    rules, tickets = open('input').read().split('\n\n', 1)
    return load_rules(rules), [[int(v) for v in l.split(',')] for l in tickets.split('\n')[1:] if len(l) and l[0] not in ['y', 'n']]

def load_rules(data):
    lines, rules = data.split('\n'), {}
    for l in lines:
        name, values = l.split(': ')
        rules[name] = [int(v) for r in values.split(' or ') for v in r.split('-')]
    return rules

def valid(value, rules):
    return sum(r[0] <= value <= r[1] or r[2] <= value <= r[3] for r in rules) > 0

def iso(rl, s = {}):
    return s if len(s) == len(rl) else iso([r - set(s.values()) for r in rl], s.update({i: list(r)[0] for i, r in enumerate(rl) if len(r) == 1}) or s)

def validForAll(rule, i, tickets):
    return sum(valid(t[i], [rule]) for t in tickets) == len(tickets)

def solve_1(rules, tickets):
    return sum(v for t in tickets for v in t if not valid(v, rules.values()))

def solve_2(rules, tickets):
    valids = [t for t in tickets if not sum(not valid(v, rules.values()) for v in t)]
    valid_rules = [set([n for n, r in rules.items() if validForAll(r, i, valids)]) for i in range(len(tickets[0]))]
    return math.prod(tickets[0][i] for i, n in iso(valid_rules).items() if n.find('departure') == 0)


rules, tickets = load_data()
# Part 1
print(solve_1(rules, tickets[1:]))
# Part 2
print(solve_2(rules, tickets))
