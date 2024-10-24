import re

def match_a_to_b(text):
    pattern = r'a.*b'
    return re.search(pattern, text) is not None

input_string = "There is a test string that ends with b"
print(match_a_to_b(input_string))
