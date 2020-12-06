def loadData(day):
	return [l.strip() for l in open('{}.data'.format(day), 'r')]

def getFields(line):
    result = set()
    parts = line.split(' ')
    for p in parts:
        result.add(p.split(':')[0])
    
    return result

def checkFields(fields, required, opt):
    return all(r in fields for r in required)
    
def solve1():
    required = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        #'cid',
    ]

    result = 0
    current_fields = set()
    for line in loadData('04'):
        if len(line) == 0:
            if checkFields(current_fields, required, []):
                result += 1
            current_fields = set()
        else:
            current_fields = current_fields.union(getFields(line))

    if checkFields(current_fields, required, []):
        result += 1
    
    return result
    
print(solve1())