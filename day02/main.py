INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [line for line in filetext.split("\n") if line]

valid = 0
for line in data:
	left, password = line.split(": ")
	bounds, letter = left.split(" ")
	a, b = map(int, bounds.split("-"))
	if a <= password.count(letter) <= b:
		valid += 1
print(valid)

valid2 = 0
for line in data:
	left, password = line.split(": ")
	bounds, letter = left.split(" ")
	a, b = map(int, bounds.split("-"))
	if (password[a-1] == letter) + (password[b-1] == letter) == 1:
		valid2 += 1
print(valid2)
