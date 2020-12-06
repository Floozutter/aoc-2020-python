INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n\n")]

from functools import reduce
in_any = 0
in_all = 0
for group in data:
	answer_sets = list(map(set, group.split()))
	in_any += len(reduce(lambda a, b: a | b, answer_sets))
	in_all += len(reduce(lambda a, b: a & b, answer_sets))
print(in_any)
print(in_all)
