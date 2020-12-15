INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [int(chunk) for chunk in filetext.strip().split(",")]

from collections import deque, defaultdict
from functools import partial
from typing import Sequence, Optional
def nth_number_spoken(starting: Sequence[int], n: int) -> int:
	if n <= len(starting):
		return starting[n - 1]
	spoken = defaultdict(partial(deque, maxlen=2))
	for i, z in enumerate(starting):
		spoken[z].append(i)
	for i in range(i + 1, n):
		z = spoken[z][-1] - spoken[z][-2] if len(spoken[z]) >= 2 else 0
		spoken[z].append(i)
	return z

print(nth_number_spoken(data, 2020))
print(nth_number_spoken(data, 30_000_000))