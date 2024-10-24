import re

def find_upper_lower_sequences(text):
    pattern = r'[A-Z][a-z]+'
    matches = re.findall(pattern, text)
    return matches

input_string = "Hello world This Is A Test"
print(find_upper_lower_sequences(input_string))
