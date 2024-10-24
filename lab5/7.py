def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

input_string = "this_is_a_snake_case_string"
print(snake_to_camel(input_string))
