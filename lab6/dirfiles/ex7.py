import os

path = open(r"C:\Users\beiba\OneDrive\Рабочий стол\кодинг\text.txt", "r")

path2 = open(r"C:\Users\beiba\OneDrive\Рабочий стол\кодинг\text2.txt", "w")

for line in path.readlines():
    path2.write(line)



