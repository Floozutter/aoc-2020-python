INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split()]

from typing import Set, Tuple, Iterator
Coordinate = Tuple[int, ...]
from itertools import product
def neighbors(coord: Coordinate) -> Iterator[Coordinate]:
	return (
		tuple(sum(pair) for pair in zip(coord, diff))
		for diff in product((-1, 0, 1), repeat = len(coord))
		if any(diff)
	)
def update(pocket: Set[Coordinate]) -> Set[Coordinate]:
	def activating(coord: Coordinate) -> bool:
		n = sum(1 for neigh in neighbors(coord) if neigh in pocket)
		if coord in pocket:
			return 2 <= n <= 3
		else:
			return n == 3
	neighs = set(neigh for active in pocket for neigh in neighbors(active))
	return set(filter(activating, pocket | neighs))

pocket3: Set[Coordinate] = set(
	(i, j, 0)
	for i, row in enumerate(data)
	for j, c in enumerate(row)
	if c == "#"
)
pocket4: Set[Coordinate] = set((i, j, k, 0) for i, j, k in pocket3)
for _ in range(6):
	pocket3 = update(pocket3)
	pocket4 = update(pocket4)
print(len(pocket3))
print(len(pocket4))
