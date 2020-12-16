INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n\n")]

from typing import Tuple
IntervalPair = Tuple[int, int, int, int]
def parse_rule(line: str) -> Tuple[str, IntervalPair]:
	field, right = line.split(": ")
	a, b, c, d = (int(z) for p in right.split("or") for z in p.split("-"))
	return field, (a, b, c, d)
def within(z: int, ip: IntervalPair) -> bool:
	return ip[0] <= z <= ip[1] or ip[2] <= z <= ip[3]
rules = dict(map(parse_rule, data[0].split("\n")))
mine = list(map(int, data[1].split("\n")[1].split(",")))
nearby = [list(map(int, line.split(","))) for line in data[2].split("\n")[1:]]

print(sum(
	value for ticket in nearby for value in ticket
	if all(not within(value, ip) for ip in rules.values())
))

valids = [
	ticket.copy() for ticket in nearby
	if all(
		any(within(value, ip) for ip in rules.values())
		for value in ticket
	)
]
field_to_indices = dict(
	(field, set(
		i for i in range(len(rules))
		if all(within(ticket[i], ip) for ticket in valids)
	))
	for field, ip in rules.items()
)
solved = set()
while any(len(indices) > 1 for indices in field_to_indices.values()):
	for indices in field_to_indices.values():
		if len(indices) == 1:
			solved.add(next(iter(indices)))
		else:
			indices -= solved
from collections import defaultdict
index_to_field = defaultdict(str, (
	(next(iter(indices)) if indices else -1, field)
	for field, indices in field_to_indices.items()
))
from math import prod
print(prod(
	value for i, value in enumerate(mine)
	if index_to_field[i].startswith("departure")
))
