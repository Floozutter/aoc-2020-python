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
	if n == 0:
		return all(a[i][c - 1] == b[i][0] for i in range(r))
	elif n == 1:
		return all(a[0][j] == b[r - 1][j] for j in range(c))
	elif n == 2:
		return all(a[i][0] == b[i][c - 1] for i in range(r))
	else:
		return all(a[r - 1][j] == b[0][j] for j in range(c))
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
from math import prod
print(prod(idn for idn, friends in friendships.items() if len(friends) == 2))
