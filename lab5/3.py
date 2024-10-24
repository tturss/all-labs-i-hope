import re

def find_lowercase_underscore(s):
    pattern = r'[a-z]+(?:_[a-z]+)*'
    return re.findall(pattern, s)

print(find_lowercase_underscore("hello_world test_string"))  
