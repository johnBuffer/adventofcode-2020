def parse_line(line):
    instr, arg = line.split(' ')
    return (instr != 'jmp') + (instr == 'jmp') * int(arg), (instr == 'acc') * int(arg), instr, int(arg)

def solve1(pgrm):
    counter, acc, executed = 0, 0, [False] * len(pgrm)
    while len(pgrm) > counter > -1 and not executed[counter]:
        executed[counter], (counter, acc) = True, map(sum, zip([counter, acc], pgrm[counter][:-2]))
    return acc, counter == len(pgrm)

def solve2(pgrm, i, done, acc):
    while not done:
        _, _, instr, arg = pgrm[i]
        idx = ['jmp', 'nop', 'acc'].index(instr)
        if idx < 2:
            acc, done = solve1(pgrm[0:i] + [(idx * arg + (not idx), 0, '', arg)] + pgrm[i+1:])
        i += 1
    return acc

program = [parse_line(l)  for l in open('08.data', 'r')]
print(solve1(program)[0])
print(solve2(program, 0, False, 0))
