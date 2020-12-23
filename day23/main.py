INPUTPATH = "input.txt"
INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
labels = list(map(int, filetext.strip()))

from typing import Optional
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
from typing import Iterator
def make_circle(labels: Iterator[int]) -> Cup:
	reversed_labels = iter(reversed(labels))
	last = Cup(next(reversed_labels))
	print(last.label)
	head = last
	for label in reversed_labels:
		print(label)
		head = Cup(label, head)
	last.succ = head
	return head
head = make_circle(labels)
