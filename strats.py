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

def devil1(enemyMoves):
    return 1

def devil2(enemyMoves):
    return 1

def devil3(enemyMoves):
    return 1

def random2_t4t(enemyMoves):
    if not enemyMoves:
        return 0
    elif len(enemyMoves)%2==0:
        return random.choice([0,1])
    return enemyMoves[-1]

def tester(enemyMoves):
    if not enemyMoves:
        return 1
    if enemyMoves[0]==1:
        return enemyMoves[-1]
    if enemyMoves[0]==0:
        if len(enemyMoves)%2==0:
            return 1
        return 0

strategies = [t4t, generoust4t, fiftyfifty, inverse_t4t, angel, devil1,devil2,devil3, random2_t4t, tester]

