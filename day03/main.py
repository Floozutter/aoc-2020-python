INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [line for line in filetext.split()]

width = len(data[0])
def trees_from_slope(right: int, down: int) -> int:
	trees = 0
	i = 0
	j = 0
	while i < len(data):
		if data[i][j % width] == "#":
			trees += 1
		i += down
		j += right
	return trees
print(trees_from_slope(3, 1))

from math import prod
print(prod((
	trees_from_slope(1, 1),
	trees_from_slope(3, 1),
	trees_from_slope(5, 1),
	trees_from_slope(7, 1),
	trees_from_slope(1, 2),
)))
