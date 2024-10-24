def insert_spaces(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

input_string = "HelloWorldThisIsAString"
print(insert_spaces(input_string))
