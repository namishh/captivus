# Split Or Steal 
import random
from strats import strategies
from player import Player
from game import Game

scores = {}
players = []

for i in strategies:
    p = Player(i)
    players.append(p)
    scores[p.name] = 0


matchups = [[a, b] for idx, a in enumerate(players) for b in players[idx + 1:]]

for k in range(10):
    rounds = random.randint(2400,2600)
    for i in matchups:
        g = Game(i, rounds)
        g.match()
        scores[i[0].name] += g.p1score 
        scores[i[1].name] += g.p2score 

    print(f"After tournament {k+1}:")
    for i in scores:
        print(f"{i}: {scores[i]}")
    print()


print(scores)
