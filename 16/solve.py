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

def solve_1(rules, tickets):
    return sum(sum(v for v in t if not valid(v, rules.values())) for t in tickets)

def isolate(valid_rules):
    res = {}
    for _ in valid_rules:
        for i, r in enumerate(valid_rules):
            if len(r) == 1:
                res[i] = list(r)[0]
                for s in valid_rules: s.discard(res[i])
    return res


def solve_2(rules, tickets):
    valid_rules = [set() for i in range(len(tickets[0]))]
    valid_tickets = [t for t in tickets if sum(valid(t[i], rules.values()) for i in range(len(t))) == len(t)]
    for i in range(len(tickets[0])):
        for name, r in rules.items():
            if sum((r[0] <= t[i] <= r[1] or r[2] <= t[i] <= r[3]) for t in valid_tickets) == len(valid_tickets):
                valid_rules[i].add(name)
    return math.prod(tickets[0][i] for i, n in isolate(valid_rules).items() if n.find('departure') == 0)
                    

rules, tickets = load_data()
print(solve_1(rules, tickets[1:]))
print(solve_2(rules, tickets))
