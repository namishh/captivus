class Player:
    def __init__(self, action) -> None:
        self.action = action
        self.points = 0
        self.name = str(action).split()[1]

    def action(self, moves):
        return self.action(moves)

    def __str__(self) -> str:
        return self.name
