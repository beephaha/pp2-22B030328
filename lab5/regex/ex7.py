import re
string = "first_name"
shablon = r"_([a-z])"
def snake_to_camel(string):
    camel = re.sub(shablon, lambda matching: matching.group(1).upper(), string)
    return camel
print(snake_to_camel(string))