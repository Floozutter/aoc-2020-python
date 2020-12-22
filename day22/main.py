INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    filetext = ifile.read()
data = [chunk for chunk in filetext.strip().split("\n\n")]

from collections import deque
from typing import Dict, Deque
Decks = Dict[str, Deque[int]]
starting: Decks = dict()
for chunk in data:
	player, cards = chunk.split(":\n")
	starting[player] = deque(map(int, cards.split()))
def copy_decks(decks: Decks) -> Decks:
	return dict((player, deque(deck)) for player, deck in decks.items())

from operator import itemgetter
def combat(decks: Decks) -> int:
	while sum(1 for deck in decks.values() if deck) > 1:
		turn = sorted(
			((player, deck.popleft()) for player, deck in decks.items()),
			key = itemgetter(1),
			reverse = True
		)
		decks[turn[0][0]].extend(list(zip(*turn))[1])
	windeck = next(filter(None, decks.values()))
	return sum((i + 1) * card for i, card in enumerate(reversed(windeck)))
print(combat(copy_decks(starting)))

from typing import FrozenSet, Tuple, Optional, Set
HashableDecks = FrozenSet[Tuple[str, Tuple[int, ...]]]
def hashableize_decks(decks: Decks) -> HashableDecks:
	return frozenset((player, tuple(deck)) for player, deck in decks.items())
def recursive_combat(decks: Decks) -> Tuple[str, int]:
	winner: Optional[str] = None
	visited: Set[HashableDecks] = set()
	while sum(1 for deck in decks.values() if deck) > 1:
		visit = hashableize_decks(decks)
		if visit in visited:
			winner = min(decks.keys())
			break
		else:
			visited.add(visit)
		turn = dict((p, d.popleft()) for p, d in decks.items())
		if all(len(decks[player]) >= card for player, card in turn.items()):
			copied_decks = copy_decks(decks)
			keeps = dict(turn)
			for player, deck in copied_decks.items():
				for _ in range(len(deck) - turn[player]):
					deck.pop()
			turn_winner = recursive_combat(copied_decks)[0]
			decks[turn_winner].append(turn[turn_winner])
			decks[turn_winner].extend(sorted(
				(c for p, c in turn.items() if p != turn_winner),
				reverse = True
			))
		else:
			order = sorted(turn.items(), key = itemgetter(1), reverse = True)
			decks[order[0][0]].extend(list(zip(*order))[1])
	if winner is None:
		winner = next(player for player, deck in decks.items() if deck)
	windeck = decks[winner]
	score = sum((i + 1) * card for i, card in enumerate(reversed(windeck)))
	return winner, score
print(recursive_combat(copy_decks(starting))[1])
