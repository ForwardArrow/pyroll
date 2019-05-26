import re

regex = r"[^hl0-9]"
testStr = "14hl"
print(re.match(regex, testStr))