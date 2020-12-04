INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [passport for passport in filetext.split("\n\n")]

def validate_hgt(s: str) -> bool:
	try:
		n = int(s[:-2])
	except ValueError:
		return False
	units = s[-2:]
	if units == "cm":
		return 150 <= n <= 193
	elif units == "in":
		return 59 <= n <= 76
	else:
		return False
def validate_hcl(s: str) -> bool:
	if len(s) == 7 and s[0] == "#":
		valid_chars = set("0123456789abcdef")
		return all(map(lambda c: c in valid_chars, s[-1:]))
	else:
		return False
def validate_pid(s: str) -> bool:
	if len(s) == 9:
		return all(map(lambda d: d in set("0123456789"), s))
	else:
		return False

valid1 = 0
valid2 = 0
for passport in data:
	fields = passport.split()
	d = dict(f.split(":") for f in fields)
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
			validate_hgt(d["hgt"]),
			validate_hcl(d["hcl"]),
			d["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
			validate_pid(d["pid"])
		)):
			valid2 += 1
print(valid1)
print(valid2)
