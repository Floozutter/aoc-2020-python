INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n\n")]

from typing import Tuple, List
def parse_rule(line: str) -> Tuple[str, List[Tuple[int, int]]]:
	field, right = line.split(": ")
	ranges = [tuple(map(int, pair.split("-"))) for pair in right.split("or")]
	return field, ranges
rules = dict(map(parse_rule, data[0].split("\n")))
mine = list(map(int, data[1].split("\n")[1].split(",")))
nearby = [list(map(int, line.split(","))) for line in data[2].split("\n")[1:]]

valids = []
error = 0
for ticket in nearby:
	valid = True
	for value in ticket:
		ok = False
		for ab, cd in rules.values():
			a, b = ab
			c, d = cd
			if a <= value <= b or c <= value <= d:
				ok = True
		if not ok:
			valid = False
			error += value
	if valid:
		valids.append(ticket)
print(error)

def within(z: int, interval: Tuple[int, int]) -> bool:
	return interval[0] <= z <= interval[1]
from collections import defaultdict
index_to_field = defaultdict(set)
for field, terval_pairs in rules.items():
	a, b = terval_pairs
	for i in range(len(mine)):
		if all(
			within(ticket[i], a) or within(ticket[i], b)
			for ticket in valids
		):
			index_to_field[i].add(field)
solved = set()
while any(len(fields) > 1 for fields in index_to_field.values()):
	for i, f in index_to_field.items():
		if len(f) == 1:
			solved.add(next(iter(f)))
		else:
			f -= solved
lol = 1
for i, v in enumerate(mine):
	if "departure" in next(iter(index_to_field[i])):
		lol *= v
print(lol)
