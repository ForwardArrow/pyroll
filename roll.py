from random import randrange

def roll_die(sides):
    return randrange(sides)+1

def roll_dice(qty, sides):
    rolls = []
    count = 0
    while count < qty:
        rolls.append(roll_die(sides))
        count += 1
    return rolls

def drop_low(rolls):
    rolls.remove(min(rolls))
    return rolls

def drop_high(rolls):
    rolls.remove(max(rolls))
    return rolls

def public_roll(qty, sides, drop='n'):
    rolls = roll_dice(qty, sides)
    if drop == 'l':
        return drop_low(rolls)
    elif drop == 'h':
        return drop_high(rolls)
    else:
        return rolls
