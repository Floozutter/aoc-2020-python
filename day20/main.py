INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n\n")]

from typing import Tuple, Iterator
Tile = Tuple[str, ...]
def rotate(t: Tile, n: int) -> Tile:
	if n == 0:
		return t
	else:
		r, c = len(t), len(t[0])
		return rotate(tuple(
			"".join(t[j][r - i - 1] for j in range(c)) for i in range(r)
		), n - 1)
def flip(t: Tile, n: int) -> Tile:
	r, c = len(t), len(t[0])
	if n == 0:
		return t
	elif n == 1:
		return tuple(
			"".join(t[r - i - 1][j] for j in range(c)) for i in range(r)
		)
	elif n == 2:
		return tuple(
			"".join(t[i][c - j - 1] for j in range(c)) for i in range(r)
		)
	else:
		return flip(flip(t, 1), 2)
def bordering(a: Tile, b: Tile, n: int) -> bool:
	r, c = len(a), len(a[0])
	if n == 0:   return all(a[i][c - 1] == b[i][0] for i in range(r))
	elif n == 1: return all(a[0][j] == b[r - 1][j] for j in range(c))
	elif n == 2: return all(a[i][0] == b[i][c - 1] for i in range(r))
	else:        return all(a[r - 1][j] == b[0][j] for j in range(c))
def borders(t: Tile) -> Iterator[str]:
	r, c = len(t), len(t[0])
	yield "".join(t[i][c - 1] for i in range(r))
	yield "".join(t[0][j] for j in range(c))
	yield "".join(t[i][0] for i in range(r))
	yield "".join(t[r - 1][j] for j in range(c))
def read_tile(chunk: str) -> Tuple[str, Tile]:
	lines = chunk.split("\n")
	return int(lines[0][5:-1]), tuple(lines[1:])
tiles = dict(map(read_tile, data))

from collections import defaultdict
borderbois = defaultdict(set)
for idn, tile in tiles.items():
	for border in borders(tile):
		borderbois[border].add(idn)
		borderbois[border[::-1]].add(idn)
friendships = defaultdict(set)
for idn in tiles.keys():
	for bois in borderbois.values():
		if idn in bois:
			friendships[idn].update(bois)
	friendships[idn].remove(idn)
corners = [idn for idn, friends in friendships.items() if len(friends) == 2]
from math import prod
print(prod(corners))

grid = dict()
grid[0, 0] = corners[3], 0, 0
solved = set()
from itertools import product
while len(solved) < len(tiles):
	items = list(grid.items())
	for key, value in items:
		if key not in solved:
			i, j = key
			idn, r, f = value
			for friend in friendships[idn]:
				for s, g, b in product(range(4), repeat = 3):
					if bordering(
						flip(rotate(tiles[idn], r), f),
						flip(rotate(tiles[friend], s), g),
						b
					):
						if b == 0:   k, l = i, j + 1  # imagine
						elif b == 1: k, l = i - 1, j  # blundering
						elif b == 2: k, l = i, j - 1  # this
						else:        k, l = i + 1, j  # >:3
						grid[k, l] = friend, s, g
						break
			solved.add(key)
indices, jndices = zip(*grid.keys())
interval = min(indices), max(indices) + 1
jnterval = min(jndices), max(jndices) + 1
step = len(next(iter(tiles.values()))) - 2
stitch = [list() for _ in range(step * (interval[1] - interval[0]))]
for h, i in enumerate(range(*interval)):
	for j in range(*jnterval):
		idn, r, f = grid[i, j]
		tile = flip(rotate(tiles[idn], r), f)
		for k, row in enumerate(tile[1: -1]):
			stitch[h * step + k].extend(row[1: -1])
image = tuple("".join(row) for row in stitch)
pattern = (
	"                  # ",
	"#    ##    ##    ###",
	" #  #  #  #  #  #   "
)
def sea_monsters(image: Tile) -> int:
	swimmies = 0
	for i in range(len(image) - len(pattern) + 1):
		for j in range(len(image[0]) - len(pattern[0]) + 1):
			if all(
				image[i + p][j + q] == "#"
				for p, row in enumerate(pattern)
				for q, c in enumerate(row)
				if c == "#"
			):
				swimmies += 1
	return swimmies
swimmies = next(filter(None, (
	sea_monsters(flip(rotate(image, r), f))
	for r, f in product(range(4), repeat = 2)
)))
print("".join(image).count("#") - "".join(pattern).count("#") * swimmies)
