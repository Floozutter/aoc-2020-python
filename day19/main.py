INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
#INPUTPATH = "input-custom.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n\n")]


from typing import Tuple, Set, Union, Iterator, Dict
Subrule = Union[str, Set[Tuple[str, ...]]]
def read_rule(r: str) -> Subrule:
	if r.startswith('"'):
		return r[1: -1]
	else:
		return set(tuple(s.split()) for s in r.split(" | "))
pairs1 = dict(line.split(": ") for line in data[0].split("\n"))
pairs2 = pairs1 | dict((("8", "42 | 42 8"), ("11", "42 31 | 42 11 31")))
rules1 = dict((k, read_rule(v)) for k, v in pairs1.items())
rules2 = dict((k, read_rule(v)) for k, v in pairs2.items())
messages = data[1].split("\n")

from itertools import combinations
def partitions(s: str, n: int) -> Iterator[Iterator[str]]:
	for indices in combinations(range(1, len(s)), n - 1):
		padded = (0,) + tuple(indices) + (len(s),)
		yield (s[i: j] for i, j in zip(padded, padded[1:]))
from functools import cache
@cache
def match(part: int, key: str, s: str) -> bool:
	rules = rules1 if part == 1 else rules2
	rule = rules[key]
	if isinstance(rule, str):
		return s == rule
	else:
		for subrule in rule:
			for partition in partitions(s, len(subrule)):
				if all(match(part, k, s) for k, s in zip(subrule, partition)):
					return True
		return False

print(sum(1 for m in messages if match(1, "0", m)))
print(sum(1 for m in messages if match(2, "0", m)))
