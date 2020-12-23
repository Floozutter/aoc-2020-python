INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
labels = list(map(int, filetext.strip()))

from typing import Optional, Iterator, Iterable
class Cup:
	label: int
	succ: "Cup"
	def __init__(self, label: int, succ: Optional["Cup"] = None) -> None:
		self.label = label
		if succ is None:
			self.succ = self
		else:
			self.succ = succ
	def insert_succ(self, cup: "Cup") -> None:
		cup.succ = self.succ
		self.succ = cup
	def remove_succ(self) -> "Cup":
		succ = self.succ
		self.succ = succ.succ
		return succ
	def labels(self) -> Iterator[int]:
		yield self.label
		cup = self.succ
		while cup != self:
			yield cup.label
			cup = cup.succ
	def cups(self) -> Iterator["Cup"]:
		yield self
		cup = self.succ
		while cup != self:
			yield cup
			cup = cup.succ
def make_circle(labels: Iterable[int]) -> Cup:
	reversed_labels = iter(reversed(list(labels)))
	head = last = Cup(next(reversed_labels))
	for label in reversed_labels:
		head = Cup(label, head)
	last.succ = head
	return head
def play(head: Cup, moves: int) -> Cup:
	cups = dict((cup.label, cup) for cup in head.cups())
	lowest, highest = min(cups), max(cups)
	for _ in range(moves):
		picked = [head.remove_succ() for _ in range(3)]
		picked_labels = {cup.label for cup in picked}
		dest = head.label - 1
		while (a := dest < lowest) or (b := dest in picked_labels):
			if a: dest = highest
			else: dest -= 1
		while picked:
			cups[dest].insert_succ(picked.pop())
		head = head.succ
	return cups[1]

print("".join(map(str, play(make_circle(labels), 100).labels()))[1:])

highest = max(labels)
from itertools import islice, chain, count
head = make_circle(islice(chain(labels, count(highest + 1)), 1_000_000))
head = play(head, 10_000_000)
print(head.succ.label * head.succ.succ.label)
