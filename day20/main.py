INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n\n")]

from typing import Tuple, Iterator, Dict, Set
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
def border(a: Tile, b: Tile, n: int) -> bool:
	r, c = len(a), len(a[0])
	if n == 0:
		return all(a[i][c - 1] == b[i][0] for i in range(r))
	elif n == 1:
		return all(a[0][j] == b[r - 1][j] for j in range(c))
	elif n == 2:
		return all(a[i][0] == b[i][c - 1] for i in range(r))
	else:
		return all(a[r - 1][j] == b[0][j] for j in range(c))
def read_tile(chunk: str) -> Tuple[str, Tile]:
	lines = chunk.split("\n")
	return int(lines[0][5:-1]), tuple(lines[1:])
tiles = dict(map(read_tile, data))

"""
from collections import defaultdict
friendships = defaultdict(set)
from itertools import product
for x in tiles.keys():
	for y in tiles.keys():
		if x != y:
			for a, b, c, d, e in product(range(4), repeat = 5):
				if border(
					flip(rotate(tiles[x], a), b),
					flip(rotate(tiles[y], c), d),
					e
				):
					friendships[x].add(y)
					break
from math import prod
print(prod(t for t, f in friendships.items() if len(f) == 2))
"""

def borders(t: Tile) -> Iterator[str]:
	r, c = len(t), len(t[0])
	yield "".join(t[i][c - 1] for i in range(r))
	yield "".join(t[0][j] for j in range(c))
	yield "".join(t[i][0] for i in range(r))
	yield "".join(t[r - 1][j] for j in range(c))
from collections import defaultdict
border_table = defaultdict(set)
for idn, tile in tiles.items():
	for border in borders(tile):
		border_table[border].add(idn)
	for border in borders(flip(tile, 3)):
		border_table[border].add(idn)
corner_product = 1
for idn in tiles.keys():
	friends = set()
	for s in border_table.values():
		if idn in s:
			friends.update(s)
	friends.remove(idn)
	if len(friends) == 2:
		corner_product *= idn
print(corner_product)
