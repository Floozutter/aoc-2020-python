INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [int(chunk) for chunk in filetext.strip().split()]

from itertools import combinations
from typing import List
def valid(pre: List[int], z: int) -> bool:
	return any(a + b == z for a, b in combinations(pre, 2))
def first_invalid(data: List[int], preamble_length: int) -> bool:
	for i in range(preamble_length, len(data)):
		if not valid(data[i - preamble_length: i], data[i]):
			return data[i]
target = first_invalid(data, 25)
print(target)

for length in range(2, len(data)):
	for i in range(0, len(data) - length + 1):
		sublist = data[i:i + length]
		if sum(sublist) == target:
			weakness = min(sublist) + max(sublist)
			break
print(weakness)
