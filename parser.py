import re

regex = r"[^hl0-9 ]"

test_str = "12d4d"

def parse(text):
    return text.split('d')

print(parse(test_str))

def validate(text_list):
    for i in text_list:
        if i.isalpha() and i not in 'lh':
            print('Invalid')
            return False
    print('Valid')
    return True
#     joinStr = ' '.join(textList)
#     print(joinStr)
#     matches = re.finditer(regex, test_str, re.MULTILINE | re.IGNORECASE)
#     if matches:
#         print('Input not Valid')
#         return False
#     else:
#         print('Input Valid')
#         return True

validate(parse(test_str))