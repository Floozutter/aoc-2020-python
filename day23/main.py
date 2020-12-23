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
	def insert_succ(self, label: int) -> None:
		self.succ = Cup(label, self.succ)
	def remove_succ(self) -> int:
		removed = self.succ
		self.succ = removed.succ
		return removed.label
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
		picks = []
		for _ in range(3):
			label = head.remove_succ()
			del cups[label]
			picks.append(label)
		dest_label = head.label - 1
		while (a := dest_label < lowest) or (b := dest_label in picks):
			if a: dest_label = highest
			else: dest_label -= 1
		dest = cups[dest_label]
		while picks:
			label = picks.pop()
			dest.insert_succ(label)
			cups[label] = dest.succ
		head = head.succ
	return cups[1]

print("".join(map(str, play(make_circle(labels), 100).labels()))[1:])

highest = max(labels)
from itertools import islice, chain, count
head = make_circle(islice(chain(labels, count(highest + 1)), 1_000_000))
head = play(head, 10_000_000)
print(head.succ.label * head.succ.succ.label)
