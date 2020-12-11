INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = sorted(int(chunk) for chunk in filetext.strip().split())

adapters = [0] + data + [data[-1] + 3]
from collections import Counter
diffs = Counter(b - a for a, b in zip(adapters[:-1], adapters[1:]))
print(diffs[1] * diffs[3])

from itertools import islice, takewhile
graph = dict(
	(a, set(takewhile(lambda b: b - a <= 3, islice(adapters, i + 1, None))))
	for i, a in enumerate(adapters)
)
from functools import cache
@cache
def paths(source: int, dest: int) -> int:
	return sum(
		1 if neighbor == dest else paths(neighbor, dest)
		for neighbor in graph[source]
	)
print(paths(adapters[0], adapters[-1]))
