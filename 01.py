def loadData(day):
	return [int(l) for l in open("{}.data".format(day), "r")]

def solve_1():
	data = loadData("01")
	
	target = 2020

	for i, n1 in enumerate(data):
		for k, n2 in enumerate(data):
			if k != i and n1 + n2 == target:
				print(n1, n2)
				return n1 * n2

	return None

def solve_2():
	data = loadData("01")
	
	target = 2020

	for i, n1 in enumerate(data):
		for j, n2 in enumerate(data):
			for k, n3 in enumerate(data):
				if k != i and i != j and n1 + n2 + n3 == target:
					print(n1, n2, n3)
					return n1 * n2 * n3

	return None

print(solve_1())
print(solve_2())