from roll import public_roll
from parser import parse

class bcolors:
    CRIT = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

roll = parse(input("Roll: "))

if len(roll) == 3: 
    qty, sides, drop = roll
    pr = public_roll(int(qty), int(sides), drop)
else:
    qty,sides = roll
    pr = public_roll(int(qty), int(sides))
output = ""
for item in pr:
    if item == int(sides):
        output += bcolors.CRIT + str(item) + bcolors.ENDC + " "
    elif item == 1:
        output += bcolors.FAIL + str(item) + bcolors.ENDC + " "
    else:
        output += str(item) + " "
print('You rolled %s %s-sided dice:' % (qty, sides))
print('[%s]' % (output.rstrip()))