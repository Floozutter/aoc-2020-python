INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split()]

buses = [int(s) if s != "x" else 0 for s in data[1].split(",")]

from typing import List
from itertools import count
def earliest(buses: List[int], start: int) -> int:
	for timestamp in count(start):
		for bus in buses:
			if bus and timestamp % bus == 0:
				return bus * (timestamp - start)
print(earliest(buses, int(data[0])))

from typing import Tuple
def xgcd(a, b) -> Tuple[int, int]:
	r_last, r = a, b
	s_last, s = 1, 0
	t_last, t = 0, 1
	while r:
		quotient = r_last // r
		r_last, r = r, r_last - quotient * r
		s_last, s = s, s_last - quotient * s
		t_last, t = t, t_last - quotient * t
	return s_last, t_last
def help(a: int, b: int, c: int, d: int) -> Tuple[int, int]:
	p = a * c
	foo, bar = xgcd(a, c)
	q = (foo * a * d + bar * c * b) % p
	return p, q
def what(buses: List[int]) -> int:
	a, b = 1, 0
	for i, bus in enumerate(buses):
		if bus:
			# (t + i) % bus = 0
			c, d = bus, (bus - i) % bus
			a, b = help(a, b, c, d)
	return b
print(what(buses))
