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

timestamp = 0
step = 1
for i, bus in filter(lambda pair: pair[1], enumerate(buses)):
	while (timestamp + i) % bus:
		timestamp += step
	step *= bus
print(timestamp)
