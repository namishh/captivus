import random 

def t4t(enemyMoves):
    if not enemyMoves:
        return 0
    return enemyMoves[-1]

def generoust4t(enemyMoves):
    if len(enemyMoves) >= 2:
        if enemyMoves[-1] == 1 and enemyMoves[-2] == 1:
            return 1
        return 0
    return 0

def fiftyfifty(enemyMoves):
    return random.choice([0,1])

def inverse_t4t(enemyMoves):
    if not enemyMoves:
        return 1
    elif enemyMoves[-1]==0:
        return 1
    return 0

def angel(enemyMoves):
    return 0

def devil(enemyMoves):
    return 1

strategies = [t4t, generoust4t, fiftyfifty, inverse_t4t, angel, devil]

