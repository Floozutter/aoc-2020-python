INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [int(line) for line in filetext.split()]

seen = set()
for a in data:
	b = 2020 - a
	if b in seen:
		break
	else:
		seen.add(a)
print(a * b)

from itertools import combinations
for x, y, z in combinations(data, 3):
	if x + y + z == 2020:
		break
print(x * y * z)
