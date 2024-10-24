import re
def replace_punctuation(text):
    return re.sub(r'[ ,.]', ':', text)

input_string = "Hello, world. How are you?"
print(replace_punctuation(input_string))
