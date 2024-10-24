import re

def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

input_string = "ThisIsACamelCaseString"
print(camel_to_snake(input_string))
