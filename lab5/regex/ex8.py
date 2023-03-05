import re
string = input()
shablon = "[A-Z]"
#print(re.split(shablon, string))
print(re.findall('[A-Z][^A-Z]*', string))