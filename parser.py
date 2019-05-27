import re

def parse(text):
    divided = text.split('d')
    if validate(divided):
        return divided

def validate(text_list):
    for i in text_list:
        if i.isalpha() and i not in 'lh':
            print('Invalid')
            return False
    return True