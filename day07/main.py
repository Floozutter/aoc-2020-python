INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n") if chunk]

from typing import Dict
rules: Dict[str, Dict[str, int]] = dict()
for line in data:
	bag, helds = line.split(" bags contain ")
	rules[bag] = dict(
		(words[1] + " " + words[2], int(words[0]))
		for words in (s.split() for s in helds.split(", "))
	) if helds != "no other bags." else dict()

def holds(bag: str, target: str) -> bool:
	return any(
		held == target or holds(held, target)
		for held in rules[bag]
	)
print(sum(1 for bag in rules if holds(bag, "shiny gold")))

def hold_count(bag: str) -> int:
	return sum(
		n * (1 + hold_count(held))
		for held, n in rules[bag].items()
	)
print(hold_count("shiny gold"))
