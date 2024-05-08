from Strategies import strategies
from Match import Match
from itertools import combinations
from random import randint

class Tournament:
    def __init__(self, maxrounds) -> None:
        self.strategies = strategies
        self.maxrounds = maxrounds
        self.database = {}

    def sorted_scores(self):
        print(sorted(self.database.items(), key=lambda x: x[1], reverse=True))

    def give_pairs(self):
        return list(combinations(self.strategies, 2))

    def round(self):
        pairs = self.give_pairs()
        rounds = randint(10000,11000)
        for i in pairs:
            p1 = i[0]()
            p2 = i[1]()
            match = Match(rounds, i[0],i[1])
            scores = match.match()
            if p1.name not in self.database:
                self.database[p1.name] = 0
            if p2.name not in self.database:
                self.database[p2.name] = 0

            self.database[p1.name] = self.database[p1.name] + scores[0]
            self.database[p2.name] = self.database[p2.name] + scores[1]

    def repeat(self):
        for _ in range(self.maxrounds):
            self.round()
