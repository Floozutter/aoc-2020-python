INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split()]

from typing import Tuple
def seat(s: str) -> Tuple[int, int]:
	row_low = 0
	row_high = 128
	for c in s[:7]:
		if c == "F":
			row_high = (row_low + row_high) // 2
		else:
			row_low = (row_low + row_high) // 2
	col_low = 0
	col_high = 8
	for c in s[-3:]:
		if c == "L":
			col_high = (col_low + col_high) // 2
		else:
			col_low = (col_low + col_high) // 2
	return (row_low, col_low)

print(max(map(lambda rc: rc[0] * 8 + rc[1], map(seat, data))))

plane = [["#"] * 8 for _ in range(128)]
for rc in map(seat, data):
	plane[rc[0]][rc[1]] = "."
for i, row in enumerate(plane):
	print(f"{''.join(row)} {i}")
