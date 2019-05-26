import re

regex = "[^hl0-9]"
teststring = "12d4dlasdf"


def Parse(text):
    return text.split('d')

print(Parse(teststring))

def Validate(textList):
    comp = re.compile(regex)
    result = re.match(comp, ''.join(textList))
    print(result)
    if result:
        print('Input not Valid')
        return False
    print('Input Valid')
    return True

Validate(Parse(teststring))