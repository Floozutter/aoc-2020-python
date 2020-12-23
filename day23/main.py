INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
cups = list(map(int, filetext.strip()))

curr = cups[0]
for _ in range(100):
	picked = []
	for _ in range(3):
		picked.append(cups.pop((cups.index(curr) + 1) % len(cups)))
	dest = curr - 1
	while dest not in cups:
		if dest < min(cups):
			dest = max(cups)
		else:
			dest -= 1
	print(curr, cups, picked, dest)
	while picked:
		cups.insert(cups.index(dest) + 1, picked.pop())
	curr = cups[(cups.index(curr) + 1) % len(cups)]
print("".join(map(str, (
	cups[(cups.index(1) + 1 + i) % len(cups)] for i in range(len(cups) - 1)
))))
