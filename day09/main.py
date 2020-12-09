INPUTPATH, N = "input.txt", 25
#INPUTPATH, N = "input-test.txt", 5
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [int(chunk) for chunk in filetext.strip().split()]

from itertools import combinations
from typing import List
def valid(pre: List[int], n: int) -> bool:
	return any(a + b == n for a, b in combinations(pre, 2))
def first_invalid(data: List[int], preamble_length: int) -> int:
	for i in range(preamble_length, len(data)):
		if not valid(data[i - preamble_length: i], data[i]):
			return data[i]
	return -1
target = first_invalid(data, N)
print(target)

def find_weakness(data: List[int], target: int) -> int:
	for i, first in enumerate(data[:-1]):
		total = first
		smallest = first
		largest = first
		for n in data[i + 1:]:
			smallest = n if n < smallest else smallest
			largest = n if n > largest else largest
			total += n
			if total == target:
				return smallest + largest
			elif total > target:
				break
	return -1
print(find_weakness(data, target))
