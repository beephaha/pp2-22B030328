import re

string = input()
shablon = '[A-Z]+[a-z]+$'

if re.search(shablon, string):
    print("FOUND!")
else:
    print("NOT FOUND!")