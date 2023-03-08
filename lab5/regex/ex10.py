import re
string = input()
def toSnake(string):
    string = re.sub(r"([A-Z])",lambda matching: "_" + matching.group(1).lower(), string)
    return string
print(toSnake(string))