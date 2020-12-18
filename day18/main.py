INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n")]

def oops(s: str) -> str:
	return s.replace("(", "?").replace(")", "(").replace("?", ")")[::-1]
def evaluate(s: str) -> int:
	s = s.strip()
	parens = 0
	for i, c in enumerate(s):
		if c == "(":
			parens += 1
		elif c == ")":
			parens -= 1
		elif c == " " and parens == 0:
			break
	if i == 0 or i == len(s) - 1:
		if s.isnumeric():
			return int(s)
		else:
			return evaluate(s[1:-1])
	left = s[:i]
	if left[0] == "(" and left[-1] == ")":
		left = left[1:-1]
	op = s[i + 1]
	right = s[i + 3:]
	if op == "*":
		return evaluate(left) * evaluate(right)
	else:
		return evaluate(left) + evaluate(right)
print(sum(evaluate(oops(line)) for line in data))

from typing import List
def tokenize(s: str) -> List[str]:
	s = s.strip()
	if s:
		parens = 0
		for i, c in enumerate(s):
			if c == "(":
				parens += 1
			elif c == ")":
				parens -= 1
			elif c == " " and parens == 0:
				break
		if i == len(s) - 1:
			return [s]
		else:
			left = s[:i]
			return [left] + tokenize(s[i:])
	else:
		return list()
def unaeval(s: str) -> int:
	if s.isnumeric():
		return int(s)
	else:
		return do(tokenize(s))
def bineval(left: str, op: str, right: str) -> int:
	if op == "+":
		return unaeval(left) + unaeval(right)
	else:
		return unaeval(left) * unaeval(right)
def do(tokens: List[str]) -> int:
	while "+" in tokens:
		i = tokens.index("+")
		res = str(bineval(*tokens[i - 1: i + 2]))
		tokens = tokens[: i - 1] + [res] + tokens[i+2:]
	while "*" in tokens:
		i = tokens.index("*")
		res = str(bineval(*tokens[i - 1: i + 2]))
		tokens = tokens[: i - 1] + [res] + tokens[i+2:]
	final = tokens[0]
	if final[0] == "(" and final[-1] == ")":
		return unaeval(final[1:-1])
	else:
		return unaeval(final)
print(sum(unaeval(line) for line in data))
