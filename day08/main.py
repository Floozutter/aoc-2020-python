INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n")]

from typing import NamedTuple, Tuple, List

class Instruction(NamedTuple):
	op: str
	arg: int

program = [Instruction(op, int(arg)) for op, arg in map(str.split, data)]

def run_program(program: List[Instruction]) -> Tuple[bool, int]:
	acc = 0
	index = 0
	visited = set()
	while index != len(program):
		if index in visited:
			return False, acc
		visited.add(index)
		inst = program[index]
		if inst.op == "acc":
			acc += inst.arg
			index += 1
		elif inst.op == "jmp":
			index += inst.arg
		else:
			index += 1
	return True, acc

print(run_program(program)[1])
 
for i, inst in enumerate(program):
	if inst.op == "nop":
		program[i] = Instruction("jmp", inst.arg)
		res = run_program(program)
		if res[0]:
			print(res[1])
			break
		program[i] = inst
	elif inst.op == "jmp":
		program[i] = Instruction("nop", inst.arg)
		res = run_program(program)
		if res[0]:
			print(res[1])
			break
		program[i] = inst
