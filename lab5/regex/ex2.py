import re

string = input()
shablon = 'ab{2,3}?'

if re.mathc(shablon, string):
    print("FOUND!")
else:
    print("NOT FOUND!")