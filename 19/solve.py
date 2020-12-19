import re

def load_data():
    rules_data, words_data = open('input').read().split('\n\n')
    return parse_rules(rules_data), [w for w in words_data.split('\n')]

def parse_rules(data):
    rules = {}
    for l in data.split('\n'):
        left, right = l.split(': ')
        if right[0] == '"': rules[left] = right[1], None, None
        else:
            if right.find(' | ') > -1:
                or_left, or_right = right.split(' | ')
                rules[left] = None, or_left.split(' '), or_right.split(' ')
            else:
                rules[left] = None, right.split(' '), None
    return rules

def build_rule(rule, all_rules, deep=0):
    if deep < 20: # my humble solution for part 2 xD
        char, left, right = all_rules[rule]
        if char is not None: 
            return char
        reg_left = ''.join([build_rule(r,  all_rules, deep + 1) for r in left])
        reg_right = '' if not right else ''.join([build_rule(r, all_rules, deep + 1) for r in right])
        return '({})'.format('|'.join(['(' + r + ')' for r in [reg_left, reg_right] if len(r)]))
    return ''


rules, words = load_data()
regex_data = '^{}$'.format(build_rule('0', rules))
# Part 1 and 2
regex = re.compile(regex_data)
print(sum(bool(regex.match(w)) for w in words))
