INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [line for line in filetext.split("\n") if line]

valid1 = 0
valid2 = 0
for line in data:
	policy, password = line.split(": ")
	numbers, letter = policy.split(" ")
	a, b = map(int, numbers.split("-"))
	if a <= password.count(letter) <= b:
		valid1 += 1
	if (password[a-1] == letter) + (password[b-1] == letter) == 1:
		valid2 += 1
print(valid1)
print(valid2)
