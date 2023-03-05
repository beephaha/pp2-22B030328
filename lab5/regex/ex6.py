import re
string = "hello, im beep."
shablon = "[ ,.]"
print(re.sub(shablon,":", string))