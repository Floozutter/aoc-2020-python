INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n\n")]

from collections import Counter
any_yes = 0
all_yes = 0
for group in data:
	people = list(group.split())
	answers = Counter("".join(people))
	any_yes += len(answers)
	all_yes += sum(1 for yeses in answers.values() if yeses == len(people))
print(any_yes)
print(all_yes)
