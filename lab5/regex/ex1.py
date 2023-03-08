import re

string = input()
shablon = r"a(b*)"

if re.search(shablon, string):
    print("FOUND!")
else:
    print("NOT FOUND!")