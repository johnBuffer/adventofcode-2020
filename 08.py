def parse_line(line):
    instr, arg = line.split(' ')
    return (instr != 'jmp') + (instr == 'jmp') * int(arg), (instr == 'acc') * int(arg), instr, int(arg)

def solve1(pgrm, counter, acc, executed, discard=False):
    while len(pgrm) > counter > -1 and not executed[counter] and not discard:
        executed[counter], (counter, acc) = True, map(sum, zip([counter, acc], pgrm[counter][:-2]))
    return acc, counter == len(pgrm)

def solve2(p, i, done, acc):
    while not done:
        _, _, istr, a = p[i]
        idx = ['jmp', 'nop', 'acc'].index(istr)
        (acc, done), i = solve1(p[0:i] + [(idx * a - idx + 1, 0, '', a)] + p[i+1:], 0, 0, [False]*len(p), idx == 2), i+1
    return acc

program = [parse_line(l)  for l in open('08.data', 'r')]
print(solve1(program, 0, 0, [False] * len(program))[0])
print(solve2(program, 0, False, 0))
