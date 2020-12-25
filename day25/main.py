INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [int(chunk) for chunk in filetext.strip().split()]
pubkey1, pubkey2 = data

from typing import Iterator
def transforms(subject: int) -> Iterator[int]:
	value = 1
	yield value
	while True:
		value *= subject
		value %= 20201227
		yield value
def search(subject: int, pubkey: int) -> int:
	for i, value in enumerate(transforms(subject)):
		if value == pubkey:
			return i
from itertools import islice
print(next(islice(transforms(pubkey2), search(7, pubkey1), None)))
