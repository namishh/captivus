from Player import Player
import random

class APJ(Player):
    def __init__(self):
        self.move = True 
        self.name = "Amaan | Apeejay School Noida"

    def pick_strategy(self):
        return self.move

    def process_results(self, my_score, my_strat, enemy_score, enemy_strat):
        if enemy_strat == False: 
            self.move = random.choices([False, True], weights=[0.9, 0.1])[0]
        else:
            self.move = True  # Cooperate if the enemy cooperated

    ## Required code to be needed under each player
    def __str__(self):
        return self.name

class AMV(Player):
    def __init__(self):
        self.move = True
        self.name = "rex | Amity International School, Mayur Vihar"

    def pick_strategy(self):
        return self.move

    def process_results(self, my_score, my_strat, enemy_score, enemy_strat):
        self.move = False

    def __str__(self):
        return self.name

class Jesus(Player):
    def __init__(self):
        self.move = True
        self.name = "Jesus | Added by nam"

    def pick_strategy(self):
        return self.move

    def process_results(self, my_score, my_strat, enemy_score, enemy_strat):
        self.move = False

    def __str__(self):
        return self.name

class PoF(Player):
    
    # testing_dur -> Number of initial moves to cooperate for
    # mirroring_dur -> Number of subsequent moves to play tit-for-tat for
    # ego -> how unforgiving to be after initial phase (b/w 0 and 1)
    # tolerance -> when to break the initial cooperation phase (b/w 0 and 1)
    
    def __init__(self, ):
        self.move = True
        self.name = f"Power of Friendship | Mayoor School, Noida"
        self.testing_dur = 6
        self.mirroring_dur = 250
        self.ego = 0.95
        self.tolerance = 0.2
        self.turn = 1 
        self.enemy_cooperations = 0
        

    def pick_strategy(self):
        self.turn += 1
        return self.move
    
    def process_results(self, my_score, my_strat, enemy_score, enemy_strat):
        
        coop_ratio = float(self.enemy_cooperations) / float(self.turn)
        self.enemy_cooperations += (1 if enemy_strat else 0)
        
        if self.turn <= self.testing_dur:
            self.move = True
            if coop_ratio < (1 - self.tolerance):
                self.move = enemy_strat
            return
        
        if self.turn <= (self.testing_dur + self.mirroring_dur):
            self.move = enemy_strat
            return
        
        if (not enemy_strat) and (coop_ratio < self.ego):
            self.move = False # retaliate
            return
        
        self.move = True
        
    def __string__(self):
        return self.name

class SNS(Player):
    def __init__(self):
        self.move = True
        self.name = "Tragedy | Shiv Nadar School, Noida"
        self.mymove =[]
        self.oppmove = []

        self.tat = False
        self.bad = False
        self.idk = False

    def process_results(self, my_score, my_strat, enemy_score, enemy_strat):
        defe = 0
        self.mymove.append(my_strat)
        self.oppmove.append(enemy_strat)
        if not self.tat and not self.bad and not self.idk:
            if len(self.mymove) <2:
                self.move = True
            elif len(self.mymove) ==2:
                self.move= False
            elif len(self.mymove) ==3:
                if enemy_strat == False:
                    self.tat= True
            elif len(self.mymove)>3:
                for z in range(len(self.oppmove)):
                    if self.oppmove[z]== False:
                        defe +=1
                if z- defe<3 or defe<2:
                    self.bad = True
                    self.move= False
                else:
                    self.idk = True
                    self.move = enemy_strat

        elif self.idk:
            self.move = enemy_strat
        elif self.bad:
            self.move = False
        elif self.tat:
            self.move = not enemy_strat

    def pick_strategy(self):
        return self.move

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

class SnekayTit4Tat(Player):

    def __init__(self):
        self.name = "Sneaky Tit 4 Tat"
        self.count = 0
        self.last_strategy = True

    def pick_strategy(self):
        return self.last_strategy

    def process_results(self, my_strategy, other_strategy, my_score, other_score):
        self.count+=1
        if self.count % 3 == 0:
            self.last_strategy = random.choice([True, False])
        else:
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

class Friedsman(Player):
    def __init__(self):
        self.name = "Friedsman"
        self.strat = True
        self.enemy_moves = []

    def pick_strategy(self):
        return self.strat
    
    def process_results(self, my_strategy, other_strategy, my_score, other_score):
        if False in self.enemy_moves:
            self.strat = False
        self.enemy_moves.append(other_strategy)

    def __str__(self) -> str:
        return self.name

class Moody(Player):
    def __init__(self):
        self.name = "Moody"
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

strategies = [Moses, Tit4Tat, GenerousTit4Tat,  Moody, InverseMoody, TitForTat_Avg, Gambler, SnekayTit4Tat, Friedsman, APJ, AMV, PoF, SNS]

