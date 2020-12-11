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
from collections import OrderedDict
visits = OrderedDict((adp, 0) for adp in adapters)
visits[adapters[0]] += 1
while visits:
	vertex, n = visits.popitem(False)
	if vertex == adapters[-1]:
		break
	else:
		for neighbor in graph[vertex]:
			visits[neighbor] += n
print(n)
