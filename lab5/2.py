import re

def match_a_bb(s):
    pattern = r'ab{2,3}'
    return re.fullmatch(pattern, s) is not None

print(match_a_bb("ab"))        # False
print(match_a_bb("abb"))       # True
print(match_a_bb("abbb"))      # True
print(match_a_bb("abbbb"))     # False
