INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n")]

from typing import List
def floating(address: str) -> List[int]:
	for i, c in enumerate(address):
		if c == "X":
			a = list(address)
			a[i] = "0"
			a = "".join(a)
			b = list(address)
			b[i] = "1"
			b = "".join(b)
			return floating(a) + floating(b)
	return [address]

memory = dict()
memory2 = dict()
for line in data:
	left, _, right = line.split()
	if left == "mask":
		mask = right
	else:
		# 1
		address = int(left[left.index("[") + 1: left.index("]")])
		value = list(f"{int(right):036b}")
		for i, c in enumerate(mask):
			if c != "X":
				value[i] = c
		memory[address] = int("".join(value), 2)
		# 2
		address2 = list(f"{address:036b}")
		for i, c in enumerate(mask):
			if c != "0":
				address2[i] = c
		for a in floating("".join(address2)):
			memory2[int(a, 2)] = int(right)
print(sum(memory.values()))
print(sum(memory2.values()))
