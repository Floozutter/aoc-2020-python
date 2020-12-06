INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n\n")]

from collections import Counter
counts1 = 0
counts2 = 0
for group in data:
	answered1 = set()
	answered2 = Counter()
	people = list(group.split())
	for person in people:
		for c in person:
			if c.isalpha():
				answered1.add(c)
				answered2[c] += 1
	counts1 += len(answered1)
	for k, v in answered2.items():
		if v == len(people):
			counts2 += 1
print(counts1)
print(counts2)
