INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split()]

arrival = int(data[0])
buses = [int(s) if s != "x" else 0 for s in data[1].split(",")]
def wait(arrival: int, bus: int) -> int:
	return bus - arrival % bus
buswaits = ((bus, wait(arrival, bus)) for bus in buses if bus)
best_bus, best_wait = min(buswaits, key = lambda pair: pair[1])
print(best_bus * best_wait)

from typing import NamedTuple
class Congruence(NamedTuple):
	mod: int
	to: int
from typing import Tuple
def bezout_coefs(a: int, b: int) -> Tuple[int, int]:
	r_last, r = a, b
	s_last, s = 1, 0
	t_last, t = 0, 1
	while r:
		quotient = r_last // r
		r_last, r = r, r_last - quotient * r
		s_last, s = s, s_last - quotient * s
		t_last, t = t, t_last - quotient * t
	return s_last, t_last
def combine_coprime(a: Congruence, b: Congruence) -> Congruence:
	mod = a.mod * b.mod
	x, y = bezout_coefs(a.mod, b.mod)
	return Congruence(mod, (x * a.mod * b.to + y * b.mod * a.to) % mod)
congruences = (
	Congruence(bus, (bus - i) % bus)
	for i, bus in enumerate(buses)
	if bus
)
from functools import reduce
print(reduce(combine_coprime, congruences).to)
