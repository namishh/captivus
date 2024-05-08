# Base Player Class
class Player:
    def __init__(self, action) -> None:
        pass
    # if not overridden, return true by default
    def action(self):
        return True

    ### Process the results of a round. This provides an opportunity to
    def process_results(self, my_strategy, other_strategy, my_score, other_score):
        pass
