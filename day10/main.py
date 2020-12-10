INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = sorted(int(chunk) for chunk in filetext.strip().split())

adapters = [0] + data + [data[-1] + 3]

from collections import Counter
diffs = Counter(b - a for a, b in zip(adapters[:-1], adapters[1:]))
print(diffs[1] * diffs[3])

from typing import List
def arrangements_brute(adapters: List[int], start: int) -> int:
	if len(adapters) <= 0:
		return 1
	else:
		a, b, c, *_ = adapters[:3] + 2 * [None]
		arr = []
		if c is not None and c - start <= 3:
			arr.append(arrangements_brute(adapters[3:], c))
		if b is not None and b - start <= 3:
			arr.append(arrangements_brute(adapters[2:], b))
		arr.append(arrangements_brute(adapters[1:], a))
		return sum(arr)
#print(arrangements_brute(adapters[1:], 0))
def arrangements(adapters: List[int], start: int) -> int:
	if len(adapters) <= 0:
		return 1
	else:
		a, b, c, *_ = adapters[:3] + 2 * [None]
		if c is not None and c - start <= 3:
			return (
				4 * arrangements(adapters[3:], c) +
				2 * arrangements(adapters[3:], b) +
				1 * arrangements(adapters[3:], a)
			)
		elif b is not None and b - start <= 3:
			return (
				2 * arrangements(adapters[2:], b) +
				1 * arrangements(adapters[2:], a)
			)
		elif a is not None and a - start <= 3:
			return arrangements(adapters[1:], a)
		else:
			return 0
		arr.append(arrangements(adapters[1:], a))
		return sum(arr)
print(arrangements(adapters[1:], 0))
