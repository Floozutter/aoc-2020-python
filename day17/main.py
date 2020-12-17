INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split()]

from typing import Set, Tuple, Iterator
Coord = Tuple[int, int, int]
active = set()
for i, row in enumerate(data):
	for j, state in enumerate(row):
		if state == "#":
			active.add((i, j, 0))

def neighbors(coord: Coord) -> Iterator[Coord]:
	uwu = (-1, 0, 1)
	for dx in uwu:
		for dy in uwu:
			for dz in uwu:
				if any((dx, dy, dz)):
					yield (coord[0] + dx, coord[1] + dy, coord[2] + dz)
def update(active: Set[Coord]) -> Set[Coord]:
	ret = set()
	uwu = set()
	for coord in active:
		uwu.add(coord)
		uwu.update(neighbors(coord))
	for coord in uwu:
		n = sum(1 for neighbor in neighbors(coord) if neighbor in active)
		if coord in active:
			if 2 <= n <= 3:
				ret.add(coord)
		else:
			if n == 3:
				ret.add(coord)
	return ret
for i in range(6):
	active = update(active)
print(len(active))

Coord2 = Tuple[int, int, int, int]
active2 = set()
for i, row in enumerate(data):
	for j, state in enumerate(row):
		if state == "#":
			active2.add((i, j, 0, 0))
def neighbors2(coord: Coord2) -> Iterator[Coord2]:
	uwu = (-1, 0, 1)
	for dx in uwu:
		for dy in uwu:
			for dz in uwu:
				for dw in uwu:
					if any((dx, dy, dz, dw)):
						yield (
							coord[0] + dx,
							coord[1] + dy,
							coord[2] + dz,
							coord[3] + dw
						)
def update2(active: Set[Coord2]) -> Set[Coord2]:
	ret = set()
	uwu = set()
	for coord in active:
		uwu.add(coord)
		uwu.update(neighbors2(coord))
	for coord in uwu:
		n = sum(1 for neighbor in neighbors2(coord) if neighbor in active)
		if coord in active:
			if 2 <= n <= 3:
				ret.add(coord)
		else:
			if n == 3:
				ret.add(coord)
	return ret
for i in range(6):
	active2 = update2(active2)
print(len(active2))
