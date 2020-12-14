INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n")]

from typing import List
def ground(floating: str) -> List[str]:
	index = floating.find("X")
	if index == -1:
		return [floating]
	else:
		a = floating[: index] + "0" + floating[index + 1:]
		b = floating[: index] + "1" + floating[index + 1:]
		return ground(a) + ground(b)

memory1 = dict()
memory2 = dict()
for line in data:
	left, _, right = line.split()
	if left == "mask":
		mask = right
	else:
		address = int(left[left.index("[") + 1: left.index("]")])
		value = int(right)
		# --- Part One ---
		memory1[address] = int("".join(
			value_bit if mask_bit == "X" else mask_bit
			for value_bit, mask_bit in zip(f"{value:036b}", mask)
		), 2)
		# --- Part Two ---
		for grounded in ground("".join(
			address_bit if mask_bit == "0" else mask_bit
			for address_bit, mask_bit in zip(f"{address:036b}", mask)
		)):
			memory2[grounded] = value
print(sum(memory1.values()))
print(sum(memory2.values()))
