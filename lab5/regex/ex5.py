import re
string = input()
shablon = 'a.*?b$'

if re.match(shablon, string):
    print("found")
else:
    print("not found")