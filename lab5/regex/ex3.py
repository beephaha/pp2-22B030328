import re
string = input()
shablon = "[a-z][_]"
if re.search(shablon, string):
    print("found")
else:
    print("not found")