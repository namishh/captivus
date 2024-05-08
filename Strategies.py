from Player import Player
import random
## True Stands For Cooperate
## False Stands for Defect

class Tit4Tat(Player):

    def __init__(self):
        self.name = "Tit 4 Tat"
        self.last_strategy = True

    def pick_strategy(self):
        return self.last_strategy

    def process_results(self, my_strategy, other_strategy, my_score, other_score):
        self.last_strategy = other_strategy

    def __str__(self) -> str:
        return self.name


class GenerousTit4Tat(Player):

    def __init__(self):
        self.name = "Generous Tit 4 Tat"
        self.hist = []
        self.last_strategy = True

    def pick_strategy(self):
        if len(self.hist) < 2:
            return self.last_strategy
        if not self.hist[-1] and not self.hist[-2]:
            return False
        return self.last_strategy

    def process_results(self, my_strategy, other_strategy, my_score, other_score):
        self.last_strategy = other_strategy
        self.hist.append(other_strategy)

    def __str__(self) -> str:
        return self.name


class Gambler(Player):
    def __init__(self):
        self.name = "Gambler"

    def pick_strategy(self):
        return random.choice([True, False])

    def __str__(self) -> str:
        return self.name

class Lucifer(Player):
    def __init__(self):
        self.name = "Lucifer"

    def pick_strategy(self):
        return False

    def __str__(self) -> str:
        return self.name

class Moses(Player):
    def __init__(self):
        self.name = "Moses"

    def pick_strategy(self):
        return True

    def __str__(self) -> str:
        return self.name

class Moody(Player):
    def __init__(self):
        self.name = "Moody"
        self.enemymoves = []
        self.move = True

    def pick_strategy(self):
        return self.move

    def process_results(self, my_strategy, other_strategy, my_score, other_score):
        if my_score >= other_score:
            self.move = True 
        else:
            self.move = False

    def __str__(self) -> str:
        return self.name


class InverseMoody(Player):
    def __init__(self):
        self.name = "Inverse Moody"
        self.enemymoves = []
        self.last_strategy = True

    def pick_strategy(self):
        return self.last_strategy 

    def process_results(self, my_strategy, other_strategy, my_score, other_score):
        if my_score >= other_score:
            self.last_strategy = False 
        else:
            self.last_strategy = True

    def __str__(self) -> str:
        return self.name

class TitForTat_Avg(Player):
    
    def __init__(self):
        self.hist = []
        self.strat = True
        self.name = "TitForTat Avg"
    
    def pick_strategy(self):
        return self.strat
    
    def process_results(self, my_strategy, other_strategy, my_score, other_score):
        if other_strategy:
            self.hist.append(1)
        else:
            self.hist.append(-1)
        total = sum(self.hist)
        if total>=0:
            self.strat = True
        else:
            self.strat = False

strategies = [Moses, Tit4Tat, GenerousTit4Tat, Lucifer, Moody, InverseMoody, TitForTat_Avg, Gambler]

