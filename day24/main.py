INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n")]

from typing import Tuple, Dict
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

black_tiles = set()
for coord in map(line_to_coordinate, data):
	black_tiles ^= {coord}
print(len(black_tiles))
