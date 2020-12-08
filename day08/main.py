INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n")]

from typing import NamedTuple
class Instruction(NamedTuple):
	op: str
	arg: int
class Termination(NamedTuple):
	good: bool
	acc: int

from typing import List
def run(program: List[Instruction]) -> Termination:
	acc = 0
	index = 0
	visited = set()
	while index != len(program):
		if index in visited:
			return Termination(False, acc)
		visited.add(index)
		inst = program[index]
		if inst.op == "acc":
			acc += inst.arg
			index += 1
		elif inst.op == "jmp":
			index += inst.arg
		else:
			index += 1
	return Termination(True, acc)

source = [Instruction(op, int(arg)) for op, arg in map(str.split, data)]
print(run(source).acc)

from typing import Optional
program = source.copy()
for i, inst in enumerate(program):
	flipop: Optional[str] = None
	if inst.op == "nop":
		flipop = "jmp"
	elif inst.op == "jmp":
		flipop = "nop"
	if flipop is not None:
		program[i] = Instruction(flipop, inst.arg)
		term = run(program)
		if term.good:
			break
		program[i] = inst
print(term.acc)
