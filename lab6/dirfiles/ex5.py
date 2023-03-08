import os

path = r"C:\Users\beiba\OneDrive\Рабочий стол\кодинг\text.txt"

list = [10, 12, 25, 56]
with open(path, 'w') as file:
    for i in range(len(list)):
        file.write(str(list[i]) + "\n")

