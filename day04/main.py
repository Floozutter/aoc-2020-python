INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.split("\n\n")]

def valid_hgt(s: str) -> bool:
	try:
		n = int(s[:-2])
	except ValueError:
		return False
	units = s[-2:]
	return any((
		units == "cm" and 150 <= n <= 193,
		units == "in" and 59 <= n <= 76
	))
def valid_hcl(s: str) -> bool:
	return len(s) == 7 and s[0] == "#" and s[1:].isalnum()
def valid_ecl(s: str) -> bool:
	return s in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
def valid_pid(s: str) -> bool:
	return len(s) == 9 and s.isnumeric()

valid1 = 0
valid2 = 0
for passport in data:
	d = dict(pair.split(":") for pair in passport.split())
	if all(map(
		lambda field: field in d,
		("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
	)):
		valid1 += 1
		if all((
			1920 <= int(d["byr"]) <= 2002,
			2010 <= int(d["iyr"]) <= 2020,
			2020 <= int(d["eyr"]) <= 2030,
			2020 <= int(d["eyr"]) <= 2030,
			valid_hgt(d["hgt"]),
			valid_hcl(d["hcl"]),
			valid_ecl(d["ecl"]),
			valid_pid(d["pid"]),
		)):
			valid2 += 1
print(valid1)
print(valid2)
