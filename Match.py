class Match:
    def __init__(self, maxrounds, prisoner_1, prisoner_2) -> None:
        self.maxrounds = maxrounds
        self.p1 = prisoner_1
        self.p2 = prisoner_2

    def score(self, strategy1, strategy2):
        if strategy1 and strategy2:
            return (3, 3)
        elif not strategy1 and strategy2:
          return (5, 0)
        elif strategy1 and not strategy2:
          return (0, 5)
        else:
          return (1, 1)

    def match(self):
        pr1 = self.p1()
        pr2 = self.p2()
        score1 = 0
        score2 = 0

        for _ in range(self.maxrounds):
            strategy1 = pr1.pick_strategy()
            strategy2 = pr2.pick_strategy()
            scores = self.score(strategy1, strategy2)
            score1 += scores[0]
            score2 += scores[1]
            pr1.process_results(strategy1, strategy2, score1, score2)
            pr2.process_results(strategy2, strategy1, score2, score1)

        return (score1, score2)


