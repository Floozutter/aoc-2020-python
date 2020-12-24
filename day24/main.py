INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n")]

from typing import Tuple, Dict, Set, Iterator, cast
Coordinate = Tuple[int, int, int]
DIRECTIONS: Dict[str, Coordinate] = {
	"e" : ( 1, -1,  0),
	"ne": ( 1,  0, -1),
	"nw": ( 0,  1, -1),
	"w" : (-1,  1,  0),
	"sw": (-1,  0,  1),
	"se": ( 0, -1,  1)
}

def line_to_coordinate(line: str) -> Coordinate:
	x, y, z = 0, 0, 0
	it = iter(line)
	for s in it:
		if s not in DIRECTIONS:
			s += next(it)
		dx, dy, dz = DIRECTIONS[s]
		x, y, z = x + dx, y + dy, z + dz
	return x, y, z
black_tiles: Set[Coordinate] = set()
for coord in map(line_to_coordinate, data):
	black_tiles ^= {coord}
print(len(black_tiles))

def neighbors(coord: Coordinate) -> Iterator[Coordinate]:
	return (
		cast(Coordinate, tuple(map(sum, zip(coord, d))))
		for d in DIRECTIONS.values()
	)
def update(black_tiles: Set[Coordinate]) -> Set[Coordinate]:
	def will_be_black(coord: Coordinate) -> bool:
		n = sum(1 for neigh in neighbors(coord) if neigh in black_tiles)
		return 1 <= n <= 2 if coord in black_tiles else n == 2
	neighs = set(neigh for tile in black_tiles for neigh in neighbors(tile))
	return set(filter(will_be_black, black_tiles | neighs))
for _ in range(100):
	black_tiles = update(black_tiles)
print(len(black_tiles))
