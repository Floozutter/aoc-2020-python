INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"

with open(INPUTPATH) as ifile:
    filetext = ifile.read()

data = [int(line) for line in filetext.split()]

numbers = set()
for n in data:
	if (2020 - n) in numbers:
		a = n
		b = 2020 - n
		break
	else:
		numbers.add(n)
print(a * b)

from itertools import combinations
for x, y, z in combinations(data, 3):
	if x + y + z == 2020:
		break
print(x * y * z)
