INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n\n")]

messages = data[1].split("\n")

lazy = dict(line.split(": ") for line in data[0].split("\n"))
rules = dict()
from itertools import product
while len(rules) < len(lazy):
	for key, value in lazy.items():
		if key not in rules:
			if value[0] == '"':
				rules[key] = set((value[1: -1],))
			else:
				subs = set(tuple(s.split()) for s in value.split(" | "))
				if all(other in rules for sub in subs for other in sub):
					rules[key] = set()
					for sub in subs:
						rules[key].update("".join(p) for p in product(*(
							rules[k] for k in sub
						)))
print(sum(1 for m in messages if m in rules["0"]))
