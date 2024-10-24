import re

def split_at_uppercase(text):
    return re.findall(r'[A-Z][^A-Z]*', text)

input_string = "HelloWorldThisIsAString"
print(split_at_uppercase(input_string))
