import os

path = r"C:\Users\beiba\OneDrive\Рабочий стол\кодинг\text.txt"

if os.path.exists(path):
    os.remove(path)