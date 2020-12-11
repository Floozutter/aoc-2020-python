INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n")]

ROW_DIFFS = (0, -1, -1, -1, 0, 1, 1, 1)
COL_DIFFS = (1, 1, 0, -1, -1, -1, 0, 1)

from typing import NamedTuple, List, Tuple, Optional, Iterator
class Area(NamedTuple):
	seats: str
	cols: int
	@staticmethod
	def from_list(li: List[str]) -> "Area":
		return Area("".join(li), len(li[0]))
	def __str__(self) -> str:
		return "\n".join(
			self.seats[r * self.cols: (r + 1) * self.cols]
			for r in range(len(self.seats) // self.cols)
		) + "\n"
	def __eq__(self, other) -> bool:
		return str(self) == str(other)
	def coords_from_index(self, index: int) -> Tuple[int, int]:
		return index // self.cols, index % self.cols
	def index_from_coords(self, r: int, c: int) -> Optional[int]:
		if 0 <= r < len(self.seats) // self.cols and 0 <= c < self.cols:
			return r * self.cols + c
		else:
			return None
	def adjacents(self, index: int) -> Iterator[str]:
		ro, co = self.coords_from_index(index)
		for rd, cd in zip(ROW_DIFFS, COL_DIFFS):
			jndex = self.index_from_coords(ro + rd, co + cd)
			if jndex is not None:
				yield self.seats[jndex]
	def visibles(self, index: int) -> Iterator[str]:
		ro, co = self.coords_from_index(index)
		for rd, cd in zip(ROW_DIFFS, COL_DIFFS):
			r, c = ro + rd, co + cd
			jndex = self.index_from_coords(r, c)
			while jndex is not None:
				if self.seats[jndex] != ".":
					yield self.seats[jndex]
					break
				r, c = r + rd, c + cd
				jndex = self.index_from_coords(r, c)
	def update(self, by_adjacents: bool) -> "Area":
		updated = list(self.seats)
		for index, seat in enumerate(updated):
			others = self.adjacents if by_adjacents else self.visibles
			occupied = sum(1 for o in others(index) if o == "#")
			if seat == "L" and occupied == 0:
				updated[index] = "#"
			elif seat == "#" and occupied >= (4 if by_adjacents else 5):
				updated[index] = "L"
		return Area("".join(updated), self.cols)
	def total_occupied(self) -> int:
		return self.seats.count("#")

def occupied_in_equilibrium(start: Area, part: int) -> int:
	last: Optional[Area] = None
	curr = start
	while last is None or curr != last:
		last = curr
		curr = curr.update(part == 1)
	return curr.total_occupied()

start = Area.from_list(data)
print(occupied_in_equilibrium(start, 1))
print(occupied_in_equilibrium(start, 2))
