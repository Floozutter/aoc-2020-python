import requests

AOC2020_URL = "https://adventofcode.com/2020/day/{?}/input"
COOKIEPATH = "sessioncookie.txt"

def get_sessioncookie() -> str:
	with open(COOKIEPATH) as ifile:
		return ifile.read()

def request_inputdottxt(url) -> str:
	nomnom = {"session": get_sessioncookie()}
	r = requests.get(url, cookies=nomnom)
	return r.text

# Prompt user for AoC day.
day = int(input("Enter Advent of Code Day: "))
assert 1 <= day <= 25, "Invalid day!"

# Request data from AoC website by formatting url.
data = request_inputdottxt(AOC2020_URL.replace("{?}", str(day)))

# Write the "input.txt" output file in the same directory.
with open("input.txt", mode="w") as ofile:
	ofile.write(data)
