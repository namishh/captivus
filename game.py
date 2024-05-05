class Game:
    def __init__(self, players, rounds) -> None:
        self.p1 = players[0]
        self.p2 = players[1]
        self.p1score = 0 
        self.p1moves = []
        self.p2score = 0
        self.p2moves = []
        self.maxrounds = rounds

    def round(self):
        actionP1 = self.p1.action(self.p2moves)
        actionP2 = self.p2.action(self.p1moves)

        self.p1moves.append(actionP1)
        self.p2moves.append(actionP2)

        #print(f"{self.p1.name}:{actionP1}\n{self.p2.name}:{actionP2}")
        
        if actionP1 == 1 and actionP2 == 0:
            self.p1score += 5
        elif actionP2 == 1 and actionP1 == 0:
            self.p2score += 5 
        elif actionP1 == 1 and actionP2 == 1:
            self.p1score += 1
            self.p2score += 1
        elif actionP1 == 0 and actionP2 == 0:
            self.p1score += 3
            self.p2score += 3 
        else:
            pass

    def scoreboard(self):
        print("Scoreboard")
        print(f"{self.p1.name}: {self.p1score}")
        print(f"{self.p2.name}: {self.p2score}\n")

    def match(self):
        for _ in range(self.maxrounds):
            self.round()
        self.scoreboard()

    def __repr__(self) -> str:
        return f'{self.p1.name}: {self.p1score} | {self.p2.name}: {self.p2score}' 
