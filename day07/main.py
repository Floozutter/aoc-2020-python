INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n") if chunk]

rules = dict()
for line in data:
	container, contained = line.split(" bags contain ")
	if contained == "no other bags.":
		rules[container] = dict()
	else:
		rules[container] = dict(
			(words[1] + " " + words[2], int(words[0]))
			for words in (s.split() for s in contained.split(", "))
		)

from typing import Set
def can_carry(
	container: str,
	contained: str,
	visited: Set[str]
) -> bool:
	visited.add(container)
	if contained in rules[container]:
		return True
	else:
		for bag in rules[container]:
			if bag not in visited and can_carry(bag, contained, visited):
				return True
		return False
print(sum(1 for bag in rules if can_carry(bag, "shiny gold", set())))

def must_carry(container: str) -> int:
	total = 0
	for bag, n in rules[container].items():
		total += n * (1 + must_carry(bag))
	return total
print(must_carry("shiny gold"))
