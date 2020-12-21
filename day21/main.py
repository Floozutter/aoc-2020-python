INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n")]

allergen_suspects = dict()
from collections import Counter
ingredient_occurrences = Counter()
for line in data:
	left, right = line.split(" (contains ")
	ingredients = set(left.split())
	allergens = set(right[:-1].split(", "))
	for a in allergens:
		if a not in allergen_suspects:
			allergen_suspects[a] = ingredients.copy()
		else:
			allergen_suspects[a] &= ingredients
	for i in ingredients:
		ingredient_occurrences[i] += 1
print(sum(
	n for i, n in ingredient_occurrences.items()
	if all(i not in suspects for suspects in allergen_suspects.values())
))

allergen_perp = dict()
while len(allergen_perp) < len(allergen_suspects):
	for a, suspects in allergen_suspects.items():
		if a not in allergen_perp:
			if len(suspects) == 1:
				allergen_perp[a] = next(iter(suspects))
			else:
				suspects -= set(allergen_perp.values())
sorted_ingredients = [allergen_perp[a] for a in sorted(allergen_perp.keys())]
print(",".join(sorted_ingredients))
