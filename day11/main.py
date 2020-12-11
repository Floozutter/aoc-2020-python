INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n")]

from typing import List
def equals(a: List[List[str]], b: List[List[str]]) -> bool:
	return "".join("".join(r) for r in a) == "".join("".join(r) for r in b)

def adjacents(seats: List[List[str]], i: int, j: int) -> List[str]:
	ret = []
	dis = [0, -1, -1, -1, 0, 1, 1, 1]
	djs = [1, 1, 0, -1, -1, -1, 0, 1]
	for di, dj in zip(dis, djs):
		ai = i + di
		aj = j + dj
		if 0 <= ai < len(seats) and 0 <= aj < len(seats[0]):
			ret.append(seats[ai][aj])
	return ret
def update(seats: List[List[str]]) -> List[List[str]]:
	newseats = [row.copy() for row in seats]
	for i in range(len(seats)):
		for j in range(len(seats[0])):
			if seats[i][j] == "L":
				if sum(1 for s in adjacents(seats, i, j) if s == "#") == 0:
					newseats[i][j] = "#"
			elif seats[i][j] == "#":
				if sum(1 for s in adjacents(seats, i, j) if s == "#") >= 4:
					newseats[i][j] = "L"
	return newseats
last = None
curr = [list(row) for row in data]
while last is None or not equals(last, curr):
	last = [row.copy() for row in curr]
	curr = update(curr)
print("".join("".join(row) for row in curr).count("#"))

def visible(seats: List[List[str]], i: int, j: int) -> List[str]:
	ret = []
	dis = [0, -1, -1, -1, 0, 1, 1, 1]
	djs = [1, 1, 0, -1, -1, -1, 0, 1]
	for di, dj in zip(dis, djs):
		ai = i + di
		aj = j + dj
		while (
			0 <= ai < len(seats) and
			0 <= aj < len(seats[0]) and
			seats[ai][aj] == "."
		):
			ai += di
			aj += dj	
		if 0 <= ai < len(seats) and 0 <= aj < len(seats[0]):
			ret.append(seats[ai][aj])
	return ret
def update2(seats: List[List[str]]) -> List[List[str]]:
	newseats = [row.copy() for row in seats]
	for i in range(len(seats)):
		for j in range(len(seats[0])):
			if seats[i][j] == "L":
				if sum(1 for s in visible(seats, i, j) if s == "#") == 0:
					newseats[i][j] = "#"
			elif seats[i][j] == "#":
				if sum(1 for s in visible(seats, i, j) if s == "#") >= 5:
					newseats[i][j] = "L"
	return newseats
last = None
curr = [list(row) for row in data]
while last is None or not equals(last, curr):
	last = [row.copy() for row in curr]
	curr = update2(curr)
print("".join("".join(row) for row in curr).count("#"))