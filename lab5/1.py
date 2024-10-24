import re

def match_a_b(s):
    pattern = r'a(b*)'
    return re.fullmatch(pattern, s) is not None

print(match_a_b("a"))          # True
print(match_a_b("ab"))         # True
print(match_a_b("abb"))        # True
print(match_a_b("ac"))         # False
