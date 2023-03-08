import os

path = r"C:\Users\beiba\OneDrive\Рабочий стол\кодинг\text.txt"

if os.path.exists(path):
    dir_name = os.path.dirname(path)
    file = os.path.basename(path)
    print("Directory:", dir_name)
    print("Filename:", file)