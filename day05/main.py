INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split()]

def seat(s: str) -> int:
	row_range = [0, 128]
	for c in s[:7]:
		row_range[c == "F"] = sum(row_range) // 2
	col_range = [0, 8]
	for c in s[-3:]:
		col_range[c == "L"] = sum(col_range) // 2
	return row_range[0] * 8 + col_range[0]
seats = list(map(seat, data))

print(max(seats))

def arithmetic_series(first: int, last: int) -> int:
	return (first + last) * (last - first + 1) // 2
print(arithmetic_series(min(seats), max(seats)) - sum(seats))
