import re

string = input()
shablon = r"a(b*)"

if re.match(shablon, string):
    print("FOUND!")
else:
    print("NOT FOUND!")