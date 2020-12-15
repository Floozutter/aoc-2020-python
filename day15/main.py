INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [int(chunk) for chunk in filetext.strip().split(",")]

from collections import defaultdict
spoken = defaultdict(list)
last = None
for i in range(2020):
	if i < len(data):
		spoke = data[i]
	elif last not in spoken or len(spoken[last]) < 2:
		spoke = 0
	else:
		spoke = spoken[last][-1] - spoken[last][-2]
	spoken[spoke].append(i)
	last = spoke
print(last)

spoken = defaultdict(list)
last = None
for i in range(30000000):
	#if (i % 1000000 == 0): print(i)
	if i < len(data):
		spoke = data[i]
	elif last not in spoken or len(spoken[last]) < 2:
		spoke = 0
	else:
		spoke = spoken[last][-1] - spoken[last][-2]
	spoken[spoke].append(i)
	if len(spoken[spoke]) > 2:
		spoken[spoke] = spoken[spoke][-2:]
	last = spoke
print(last)