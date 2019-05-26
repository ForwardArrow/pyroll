from random import randrange

def RollDie(sides):
    return randrange(sides)+1

def RollDice(qty, sides):
    rolls = []
    count = 0
    while count < qty:
        rolls.append(RollDie(sides))
        count += 1
    return rolls

def DropLow(rolls):
    rolls.remove(min(rolls))
    return rolls

def DropHigh(rolls):
    rolls.remove(max(rolls))
    return rolls

def PublicRoll(qty, sides, drop='n'):
    rolls = RollDice(qty, sides)
    if drop == 'l':
        return DropLow(rolls)
    elif drop == 'h':
        return DropHigh(rolls)
    else:
        return rolls
