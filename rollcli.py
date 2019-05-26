from roll import PublicRoll

class bcolors:
    CRIT = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

qty = 3
sides = 15
output = ""
for item in PublicRoll(qty,sides):
    if item == sides:
        output += bcolors.CRIT + str(item) + bcolors.ENDC + " "
    elif item == 1:
        output += bcolors.FAIL + str(item) + bcolors.ENDC + " "
    else:
        output += str(item) + " " 
print('You rolled %s %s-sided dice:' % (qty, sides))
print('[%s]' % (output.rstrip()))