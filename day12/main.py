INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split()]

from typing import NamedTuple, List
class Instruction(NamedTuple):
	action: str
	value: int
route = [Instruction(s[0], int(s[1:])) for s in data]

def run1(route: List[Instruction]) -> int:
	x, y = 0, 0
	heading = 0
	for inst in route:
		if inst.action == "E":
			x += inst.value
		elif inst.action == "N":
			y += inst.value
		elif inst.action == "W":
			x -= inst.value
		elif inst.action == "S":
			y -= inst.value
		elif inst.action == "L":
			heading = (heading + inst.value) % 360
		elif inst.action == "R":
			heading = (heading - inst.value) % 360
		elif inst.action == "F":
			if heading == 0:
				x += inst.value
			elif heading == 90:
				y += inst.value
			elif heading == 180:
				x -= inst.value
			elif heading == 270:
				y -= inst.value
	return abs(x) + abs(y)
print(run1(route))

def run2(route: List[Instruction]) -> int:
	x, y = 0, 0
	a, b = 10, 1
	for inst in route:
		if inst.action == "E":
			a += inst.value
		elif inst.action == "N":
			b += inst.value
		elif inst.action == "W":
			a -= inst.value
		elif inst.action == "S":
			b -= inst.value
		elif inst.action == "L":
			for _ in range(inst.value // 90):
				a, b = -b, a
		elif inst.action == "R":
			for _ in range(inst.value // 90):
				a, b = b, -a
		elif inst.action == "F":
			x += a * inst.value
			y += b * inst.value
	return abs(x) + abs(y)
print(run2(route))
